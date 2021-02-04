# if you use this code please give credit to Konstantinos Karakasidis
import pyautogui as p
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog
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
        self.root.iconbitmap("icon.ico")
        self.widgets()
        win_width = root.winfo_reqwidth()
        win_hight = root.winfo_reqheight()
        pos_right = int(root.winfo_screenwidth()/3 - win_width/3)
        pos_down = int(root.winfo_screenheight()/3 - win_hight/3)
        root.geometry("280x100+{}+{}".format(pos_right, pos_down))


    def widgets(self):
        #basiko para8iro
        self.bt_text = 'Simple Print Screen'
        self.font = 'Arial 15 bold'
        self.error = tk.StringVar()
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=1, fill='both')
        self.canvas = tk.Canvas(self.frame, bg='lightgray')
        self.canvas.pack(expand=1, fill='both')
        #dimiourgia antikimenon ston camva
        self.button1 = tk.Button(self.canvas, text=self.bt_text, font='Arial 12', command=self.screenShot, width=18, anchor='s')
        self.button1.pack()
        self.button2 = tk.Button(self.canvas, text='Έξοδος', font='Arial 12', command=self.root.destroy, width=10, anchor='s')
        self.button2.pack()
        self.buttoni = tk.Button(self.canvas, text='About ', font='Arial 8 bold', width=4, command=self.info, anchor='s')
        self.buttoni.pack()
        #topothetish antikimenon ston camva
        self.pos_b1 = self.canvas.create_window(140,70, window=self.button1)
        self.pos_b2 = self.canvas.create_window(275, 5, anchor='ne', window=self.button2)
        self.pos_bi = self.canvas.create_window(5, 5, anchor='nw', window=self.buttoni)

        # self.root.bind('<Enter>', self.screenShot())

    def info(self):
        simpledialog.messagebox.showinfo('About', ' Simple Print Screen version 1 \n Credits: \n Κωνσταντίνος Καρακασίδης')

    def screenShot(self):
        now = datetime.now()
        n = now.strftime("_%H-%M-%S_%B_%d_%Y")
        ss = p.screenshot(f'images/SimplePrintScreen{n}.png')
        # return ss



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
