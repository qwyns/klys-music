import os, glob, re, time

from .utils.TimedProcess import TimedProcess

from eyed3.utils.console import ProgressBar

@TimedProcess("playlist processing")
def processPlaylists(musicDir, playlistDir):
    print (musicDir)
    print (playlistDir)
    # Create a subplaylist folder
    os.makedirs(os.path.realpath(os.path.join(playlistDir, 'Individual')), exist_ok=True)

    # Get possible formats
    formats = ['flac', 'mp3', 'm4a', 'wma', 'wav']
    possible_formats = set()
    total_songs = 0
    for (p, _, f) in os.walk(musicDir):
        possible_songs = [m.group(1).lower() for m in [re.match(r'.*[.](.*)', n) for n in f] if m]
        possible_formats = possible_formats | {*possible_songs}
        total_songs += len([s for s in possible_songs if s in formats])
    print (f"Formats used: [{', '.join(sorted(list([f for f in possible_formats if f in formats])))}]\nFormats present, but ignored: [{', '.join(sorted(list([f for f in possible_formats if f not in formats])))}]")

    with open(os.path.realpath(os.path.join(playlistDir, 'overall.m3u')), 'w') as opl:
        pb = ProgressBar(total_songs)
        for (p, _, f) in os.walk(musicDir):
            if p == musicDir:
                continue
            for (_, _, sf) in os.walk(p):
                music = list(map(lambda x: os.path.join(os.getcwd(), x), filter(lambda x: any([fo in x.split('.')[-1].lower() for fo in formats]), sf)))
            if music:
                with open(os.path.join(playlistDir, 'Individual', os.path.split(p)[1]) + ".m3u", "w") as pl:
                    for m in music:
                        pl.write(m + "\n")
                        opl.write(m + "\n")
                        pb.update()
        pb.__exit__(None, None, None)

def main(songsDir, playlistsDir):
    # Start Processing
    processPlaylists(songsDir, playlistsDir)


if __name__ == '__main__':
    main(os.path.join(os.getcwd(), '..'), os.getcwd())