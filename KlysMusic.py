import os, platform
from modules import KlysD3, KlysStats, KlysPlaylist
from modules.utils.FileChooser import FileChooser

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
        print("Choose the folder to get stats for:")
        KlysStats.main(FileChooser(parentDir))
        mainLoop()
    elif cmd == '2':
        print("Choose the folder to perform ID3 retagging for:")
        KlysD3.main(FileChooser(parentDir))
        mainLoop()
    elif cmd == '3':
        print("Choose the folder containing music:")
        musicDir = FileChooser(parentDir)
        print("Choose the folder to output Playlists to:")
        playlistDir = FileChooser(currentDir)
        KlysPlaylist.main(musicDir, playlistDir)
        mainLoop()
    else:
        print ("Exiting...")

        
if __name__ == '__main__':
    mainLoop()