import os
import math
import sys


def FileChooser(i):
    PrintDirectories(os.path.realpath(i))
    choice = input(f"\r{os.path.realpath(i)} $")
    if choice == "." or choice == "":
        return i
    else:
        n = os.path.realpath(os.path.join(i, choice))
        if os.path.isdir(n):
            return FileChooser(n)
        else:
            print(f"{choice} is not a valid directory")
            return FileChooser(i)


def PrintDirectories(i):
    dirlist = ['. (Choose)', '.. (Parent)', *
               [f.name for f in os.scandir(i) if f.is_dir()]]
    longest_name_len = max([len(_) for _ in dirlist])
    entries_per_row = math.ceil(140/(longest_name_len + 4))
    print('\n'.join([''.join((*map(lambda x: x.ljust(longest_name_len + 4), dirlist[_:_+entries_per_row]), ))
                     for _ in range(0, len(dirlist), entries_per_row)]))
