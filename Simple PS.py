# if you use this code please give credit to Konstantinos Karakasidis
import pyautogui as p
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog
import os
import PySimpleGUIQt as sg
import threading
# ------------------------------MS imports for admin privileges start---------------------------------------------------
import ctypes
import enum
import sys
# ------------------------------MS imports for admin privileges end-----------------------------------------------------


class App():
    def __init__(self, root):
        #ri8misis - 8esh para8iroy
        self.root = root
        root.title("Simple Print Screen")
        root.resizable(False,False)
        # root.protocol("WM_DELETE_WINDOW", root.iconify)
        self.root.iconbitmap("icon.ico")
        self.widgets()
        win_width = root.winfo_reqwidth()
        win_hight = root.winfo_reqheight()
        pos_right = int(root.winfo_screenwidth()/3 - win_width/3)
        pos_down = int(root.winfo_screenheight()/3 - win_hight/3)
        root.geometry("280x145+{}+{}".format(pos_right, pos_down))

    def widgets(self):
        #basiko para8iro
        self.font = 'Arial 12'
        self.error = tk.StringVar()
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=1, fill='both')
        self.canvas = tk.Canvas(self.frame, bg='lightgray')
        self.canvas.pack(expand=1, fill='both')
        #dimiourgia antikimenon ston camva
        self.button1 = tk.Button(self.canvas, text='Simple Print Screen', font=self.font, command=self.screenShot, width=29, anchor='s')
        self.button1.pack()
        self.button2 = tk.Button(self.canvas, text='Έξοδος', font=self.font, command=self.root.destroy, width=29, anchor='s')
        self.button2.pack()
        self.buttonTray = tk.Button(self.canvas, text='Εικονίδιο στη γραμμή εργασιών', font=self.font, width=29, command=self.tray_stat,anchor='s')
        self.buttonTray.pack()
        self.buttoni = tk.Button(self.canvas, text='About ', font=self.font, width=29, command=self.info, anchor='s')
        self.buttoni.pack()
        #topothetish antikimenon ston camva
        self.pos_b1 = self.canvas.create_window(5,5, anchor='nw', window=self.button1)
        self.pos_b2 = self.canvas.create_window(5, 110, anchor='nw', window=self.button2)
        self.pos_bi = self.canvas.create_window(5, 75, anchor='nw', window=self.buttoni)
        self.pos_tray = self.canvas.create_window(5, 40, anchor='nw', window=self.buttonTray)

    def refresh(self):
        self.root.update()
        self.root.after(1, self.refresh)

    def tray_stat(self):
        self.refresh()
        self.root.destroy()
        self.thread = threading.Thread(target=self.systray(), daemon=True)
        self.thread.start()

    def info(self):
        simpledialog.messagebox.showinfo('About', ' Simple Print Screen version 2 \n Credits: \n Κωνσταντίνος Καρακασίδης')

    def screenShot(self):
        if os.path.isdir('images') is not True: os.mkdir('images')
        now = datetime.now()
        n = now.strftime("_%H-%M-%S_%B_%d_%Y")
        p.screenshot(f'images/SimplePrintScreen{n}.png')

    def systray(self):
        menu_def = ['BLANK', ['&Άνοιγμα', '&Έξοδος']]
        tray = sg.SystemTray(menu=menu_def, filename=r'icon.ico', tooltip='click for Simple Print Screen')
        while True:
            menu_item = tray.Read()
            if menu_item == 'Έξοδος':
                break
            elif menu_item == 'Άνοιγμα':
                bootstrap()
            elif menu_item == '__ACTIVATED__':
                self.screenShot()


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
        root = tk.Tk()
        App(root)
        root.mainloop()

    else:
        hinstance = ctypes.windll.shell32.ShellExecuteW(
            None, 'runas', sys.executable, sys.argv[0], None, SW.SHOWNORMAL
        )
        if hinstance <= 32:
            raise RuntimeError(ERROR(hinstance))

# ------------------------------MS code for admin privileges end--------------------------------------------------------

if __name__ == '__main__':
    app = bootstrap()
