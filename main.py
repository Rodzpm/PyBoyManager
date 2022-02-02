from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk
from os import listdir
from os.path import isfile, join
from pyboy import PyBoy, WindowEvent
from functools import partial
from time import sleep

class App:
    def __init__(self, dimensions, app_theme):
        self.dimensions = dimensions
        self.app_theme = app_theme
        self.root = ThemedTk(theme=self.app_theme)
        self.root.geometry(self.dimensions)
        self.root.configure(background="#E7E7E7")
    def run(self):
        st = ttk.Style()
        st.configure('W.TButton', background='#E7E7E7', foreground='#6F6F6F', font=("Lucida Grande",30))
        #NAVBAR
        ttk.Label(self.root,text="PyBoyManager",background="#E7E7E7",foreground="#6F6F6F",font=("Lucida Grande",30,"bold")).grid(row=0,column=0,padx=10)
        ttk.Button(self.root,text="Add ROMS",style='W.TButton').grid(row=0,column=1,padx=10)
        ttk.Button(self.root,text="Exit",style='W.TButton',command=self.root.destroy).grid(row=0,column=2,padx=10)
        #ROMS
        roms = [f for f in listdir("ROMS") if isfile(join("ROMS", f))]
        roms_title = [f[:-3] for f in listdir("ROMS") if isfile(join("ROMS", f))]
        r = 1
        c = 0
        i = 0
        for game in roms_title:
            if roms[i][-2:] == "gb" or roms[i][-2:] == "GB":
                if c == 3:
                    r += 1
                    c = 0
                F = ttk.Frame(self.root).grid(row=r, column=c,padx=10,pady=20)
                ttk.Label(F,text=game,background="#E7E7E7",foreground="#6F6F6F",font=("Lucida Grande",15)).grid(row=r+1,column=c)
                ttk.Button(F,text="Play",style='W.TButton',command=partial(self.Emulator, roms[i])).grid(row=r+2,column=c)
                c+=1
            i += 1
        self.root.mainloop()

    def Emulator(self,game):
        self.root.destroy()
        pyboy = PyBoy("ROMS/"+game)
        while not pyboy.tick():
            pass
        pyboy.stop()
        main()

def main():
    win = App("850x800","yaru")
    win.run()



if "__main__" == __name__:
    main()



"""
A = A
B = S
Start = Enter
Select = Backspace
Speed = Spacebar
Save = Z
Load Save = X
"""