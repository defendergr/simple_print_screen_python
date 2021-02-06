# if you use this code please give credit to Konstantinos Karakasidis
import pyautogui as p
from datetime import datetime
import os
# ------------------------------MS imports for admin privileges start---------------------------------------------------
import ctypes
import enum
import sys
# ------------------------------MS imports for admin privileges end-----------------------------------------------------


class App():
    def __init__(self):
        self.screenShot()

    def screenShot(self):
        if os.path.isdir('images') is not True: os.mkdir('images')
        now = datetime.now()
        n = now.strftime("_%H-%M-%S_%B_%d_%Y")
        p.screenshot(f'images/SimplePrintScreen{n}.png')

# ------------------------------MS code for admin privileges start------------------------------------------------------
class SW(enum.IntEnum):

    HIDE = 0
    MAXIMIZE = 3
    MINIMIZE = 6
    RESTORE = 9
    SHOW = 5
    SHOWDEFAULT = 10
    SHOWMAXIMIZED = 3
    SHOWMINIMIZED = 2
    SHOWMINNOACTIVE = 7
    SHOWNA = 8
    SHOWNOACTIVATE = 4
    SHOWNORMAL = 1


class ERROR(enum.IntEnum):

    ZERO = 0
    FILE_NOT_FOUND = 2
    PATH_NOT_FOUND = 3
    BAD_FORMAT = 11
    ACCESS_DENIED = 5
    ASSOC_INCOMPLETE = 27
    DDE_BUSY = 30
    DDE_FAIL = 29
    DDE_TIMEOUT = 28
    DLL_NOT_FOUND = 32
    NO_ASSOC = 31
    OOM = 8
    SHARE = 26


def bootstrap():
    if ctypes.windll.shell32.IsUserAnAdmin():
        App()
    else:
        hinstance = ctypes.windll.shell32.ShellExecuteW(
            None, 'runas', sys.executable, sys.argv[0], None, SW.SHOWNORMAL
        )
        if hinstance <= 32:
            raise RuntimeError(ERROR(hinstance))

# ------------------------------MS code for admin privileges end--------------------------------------------------------

if __name__ == '__main__':
    app = bootstrap()
