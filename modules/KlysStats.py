import datetime, functools, logging, math, operator, os, re, sys

from .utils.TimedProcess import TimedProcess

# Constants
DEBUG = False
FORMATS = ['mp3', 'flac', 'wav', 'm4a', ]


LOG_LENGTH = 140
LOG_HORI = '─'
LOG_VERT = '│'
LOG_TOP_LEFT = '┌'
LOG_TOP_RIGHT = '┐'
LOG_MIDDLE_LEFT = '├'
LOG_MIDDLE_RIGHT = '┤'
LOG_BOTTOM_LEFT = '└'
LOG_BOTTOM_RIGHT = '┘'
LOG_CENTRE_START = '┬'
LOG_CENTRE_END = '┴'
LOG_CENTRE = '┼'


class JobLogger:
    def log(self, s: str, cr: bool = False):
        sys.stdout.write(
            (s.ljust(LOG_LENGTH - 4).center(LOG_LENGTH - 2).center(LOG_LENGTH, LOG_VERT)) + ('\r' if cr else '\n'))

    def startLog(self):
        self.log(LOG_TOP_LEFT + ''.center(LOG_LENGTH -
                                          2, LOG_HORI) + LOG_TOP_RIGHT)

    def endLog(self):
        self.log(LOG_BOTTOM_LEFT + ''.center(LOG_LENGTH -
                                             2, LOG_HORI) + LOG_BOTTOM_RIGHT)

    def breakLog(self):
        self.log(LOG_MIDDLE_LEFT + ''.center(LOG_LENGTH -
                                             2, LOG_HORI) + LOG_MIDDLE_RIGHT)

    def logCentre(self, s: str):
        self.log((f'{s}').center(LOG_LENGTH - 2).center(LOG_LENGTH, LOG_VERT))

    def progress(self, p: float):
        self.log(
            ''.rjust(int(p * (LOG_LENGTH - 4)),
                     '█').ljust(LOG_LENGTH - 4, '░'),
            True)

@TimedProcess("stats processing")
def processFolder(path):
    # Find folder name
    if (os.path.isdir(path)):
        folder = os.path.basename(path)
    else:
        print(f'[{path}] is not a directory')
        return

    l = JobLogger()
    l.startLog()
    l.logCentre('Klys Music Stats')
    l.breakLog()

    # Find Directories
    dirs = set()
    formats = set()
    for d in os.listdir(path):
        if os.path.isdir(os.path.join(path, d)) and (not d in ['Playlists', 'Individual']):
            dirs.add(os.path.join(path, d))

    # Calculate dirs
    cdirs = []
    totalsize = 0
    totalcount = 0
    for d in dirs:
        s = 0
        c = 0
        for f in os.listdir(d):
            if os.path.isfile(os.path.join(d, f)) and f.split('.')[-1].lower() in FORMATS:
                formats.add(f.split('.')[-1])
                s += os.path.getsize(os.path.join(d, f))
                c += 1
        totalsize += s
        totalcount += c
        if s > 0:
            cdirs.append((d, s, c))

    # Sort and print dirs
    l.log(f'{str(round(totalsize / (1024 ** 2), 2)).ljust(6)} mb in {totalcount} songs in {len(cdirs)} directories:')
    ml = functools.reduce(lambda a, c: max(a, len(c[0])), cdirs, 0)

    # Table Head
    sys.stdout.write(f'{LOG_MIDDLE_LEFT}{"".ljust(ml + 3, LOG_HORI)}{LOG_CENTRE_START}{"".ljust(9, LOG_HORI)}{LOG_CENTRE_START}{"".ljust(11, LOG_HORI)}{LOG_CENTRE_START}{"".ljust(10, LOG_HORI)}{LOG_CENTRE_START}{"".ljust(LOG_LENGTH - ml - 39, LOG_HORI)}{LOG_MIDDLE_RIGHT}\n')
    sys.stdout.write(f'{LOG_VERT} {"Folder".ljust(ml + 1, )} {LOG_VERT} {"Songs".ljust(7)} {LOG_VERT} {"Size".ljust(9)} {LOG_VERT} {"Size".ljust(8)} {LOG_VERT} {"Size".ljust(LOG_LENGTH - ml - 41)} {LOG_VERT} \n')
    sys.stdout.write(f'{LOG_MIDDLE_LEFT}{"".ljust(ml + 3, LOG_HORI)}{LOG_CENTRE}{"".ljust(9, LOG_HORI)}{LOG_CENTRE}{"".ljust(11, LOG_HORI)}{LOG_CENTRE}{"".ljust(10, LOG_HORI)}{LOG_CENTRE}{"".ljust(LOG_LENGTH - ml - 39, LOG_HORI)}{LOG_MIDDLE_RIGHT}\n')

    # Table Body
    for (d, s, c) in sorted(cdirs, key=operator.itemgetter(1), reverse=True):
        l.log(f'{d.ljust(ml + 1)} {LOG_VERT} {str(c).ljust(7)} {LOG_VERT} {str(round(s / (1024 ** 2), 2)).ljust(6)} mb {LOG_VERT} {str(round(s/totalsize * 100, 2)).ljust(6)} % {LOG_VERT} {"".ljust(math.ceil((LOG_LENGTH - ml - 32) * (s/totalsize)), "▀")}')

    # Table Footer
    sys.stdout.write(f'{LOG_BOTTOM_LEFT}{"".ljust(ml + 3, LOG_HORI)}{LOG_CENTRE_END}{"".ljust(9, LOG_HORI)}{LOG_CENTRE_END}{"".ljust(11, LOG_HORI)}{LOG_CENTRE_END}{"".ljust(10, LOG_HORI)}{LOG_CENTRE_END}{"".ljust(LOG_LENGTH - ml - 39, LOG_HORI)}{LOG_BOTTOM_RIGHT}\n')


def main(dirToCheck):
    # Start Processing
    processFolder(dirToCheck)


if __name__ == '__main__':
    # Go to parent directory
    os.chdir('..')

    main(os.getcwd())
