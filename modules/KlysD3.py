import os, sys, re, datetime, logging
from eyed3 import load as ID3
from eyed3.utils.console import ProgressBar

from .utils.TimedProcess import TimedProcess

# Suppress warnings
logging.getLogger("eyed3.mp3.headers").setLevel(logging.CRITICAL)

# Constants
DEBUG = False




def processSong(s, album=None, artist=None, title=None):
    # Find artist and title from name
    if not (artist and title):
        split_name = re.match(r'(?P<artist>.*?) - (?P<title>.*?)[.]', os.path.basename(s))
        if not split_name:
            return False
        artist = split_name.group('artist') if not artist else artist
        title = split_name.group('title') if not title else title

    # Find album from folder name
    if not album:
        album = os.path.basename(os.path.dirname(s)) if os.path.isdir(os.path.dirname(s)) else "No Album"
    
    # Create ID3
    id3 = ID3(s)
    if id3 is None:
        return False
    
    # Modify tag data
    try:
        id3.initTag()
        id3.tag.comments.set(u"Tagged by Klys' Music Tools")
        id3.tag.artist = artist
        id3.tag.album = album
        id3.tag.title = title
        id3.tag.genre = u''
        if not DEBUG:
            id3.tag.save(version=(2, 4, 0))
    except:
        print (f'Exception in {s}')
    finally:    
        return True

@TimedProcess("ID3 retagging")
def processFolder(path):
    # Find folder name
    if (os.path.isdir(path)):
        folder = os.path.basename(path)
    else:
        print (f'[{path}] is not a directory')
        return
        
    # Find songs from folders
    songs = []
    for (p, d, f) in os.walk(path):
        songs.extend([os.path.join(p, x) for x in f if ((os.path.isfile(os.path.join(p, x))) and (x[-3:] == 'mp3'))])
    ProgressBar.map(processSong, songs)
            
        
def main(dirToCheck):
    # Start Processing
    processFolder(dirToCheck)

if __name__ == '__main__':
    # Go to parent directory
    os.chdir('..')

    main(os.getcwd())
