from win10toast import ToastNotifier
import PySimpleGUIQt as sg
import os
from datetime import datetime
import threading
import pyautogui as p
# ------------------------------MS imports for admin privileges start---------------------------------------------------
import ctypes
import enum
import sys
# ------------------------------MS imports for admin privileges end-----------------------------------------------------


class App():
    def __init__(self):
        self.tray_start()

    def tray_start(self):
        self.thread1 = threading.Thread(target=self.notification(), daemon=True).start()
        self.thread2 = threading.Thread(target=self.systray(), daemon=True).start()


    def screenShot(self):
        home = os.environ.get('USERPROFILE')
        dir = 'Simple Print Screen'
        if os.path.isdir(home+'/'+dir) is not True:
            path = os.path.join(home,dir)
            os.mkdir(path)
        now = datetime.now()
        n = now.strftime("_%H-%M-%S_%B_%d_%Y")
        p.screenshot(home+f'/Simple Print Screen/SimplePrintScreen{n}.png')

    def systray(self):
        menu_def = ['BLANK', ['&Άνοιγμα φακέλου', '&Πληροφορίες', '&Έξοδος']]
        tray = sg.SystemTray(menu=menu_def, filename=r'icon.ico', tooltip='Κλικ για Simple Print Screen')
        while True:
            menu_item = tray.Read()
            if menu_item == 'Έξοδος':
                break
            elif menu_item == 'Άνοιγμα φακέλου':
                home = os.environ.get('USERPROFILE')
                dir = 'Simple Print Screen'
                if os.path.isdir(home + '/' + dir) is not True:
                    path = os.path.join(home, dir)
                    os.mkdir(path)
                os.startfile(home+'/'+dir)
            elif menu_item == '__ACTIVATED__':
                self.screenShot()
                self.notificationSave()
            elif menu_item == 'Πληροφορίες':
                sg.Popup(' Πληροφορίες', ' Simple Print Screen Έκδοση 3.2 \n\n Ευχαριστώ που χρησιμοποιείτε την εφαρμογή. \n Η εφαρμογή αναπτύχθηκε από τον \n Κωνσταντίνο Καρακασίδη. \n\n Επικοινωνία: defendergr@gmail.com \n', icon='icon.ico')

    def notification(self):
        toaster = ToastNotifier()
        toaster.show_toast('Simple Print Screen', 'Από: \nΚωνσταντίνος Καρακασίδης', duration=3, icon_path='icon.ico')

    def notificationSave(self):
        toaster = ToastNotifier()
        toaster.show_toast('Simple Print Screen', 'Το στιγμιότυπο οθόνης αποθηκεύτηκε', duration=2, icon_path='icon.ico')


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
