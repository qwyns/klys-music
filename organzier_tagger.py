import os
import glob
import re

import eyed3

# Change to parent directory
cdir = os.getcwd()
os.chdir('..')
pdir = os.getcwd()
os.chdir(cdir)

# Pick only specific formats
formats = 'mp3'

for (p, d, f) in os.walk(pdir):
    if (p == pdir) or (cdir in p):
        continue
    else:
        os.chdir(p)
        for (sp, sd, sf) in os.walk(p):
            print (sp)
            songs = list(map(lambda x: os.path.join(os.getcwd(), x), filter(lambda x: x[-3:] == formats, sf)))
            id3songs = filter(lambda x: x is not None, map(lambda x: eyed3.load(x), songs))
#            for id3 in id3songs:
#                print (id3.tag.artist)
#                print (id3.tag.album)

