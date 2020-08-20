import os, platform
from modules import KlysD3, KlysStats, KlysPlaylist

def clearScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def mainLoop():
    currentDir = os.getcwd()
    parentDir = os.path.realpath(os.path.join(os.getcwd(), '..'))
    cmd = input("1: Stats\n2: ID3 retagging\n3: Playlist regeneration\nSelect option to continue or anything else to exit\n")
    clearScreen()
    if cmd == '1':
        KlysStats.main(parentDir)
        mainLoop()
    elif cmd == '2':
        KlysD3.main(parentDir)
        mainLoop()
    elif cmd == '3':
        KlysPlaylist.main(parentDir, currentDir)
        mainLoop()
    else:
        print ("Exiting...")

        
if __name__ == '__main__':
    mainLoop()