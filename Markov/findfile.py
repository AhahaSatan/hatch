import os
from functools import partial
from tkinter import *
from textparser import Parser
class Findfile:
    def __init__(self, parser):
        self.parser = parser
        self.root = Tk()
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill = Y)
        self.F = Canvas(self.root, yscrollcommand=self.scrollbar.set)
        self.F.pack(side=LEFT, fill = BOTH)
        self.scrollbar.config(command=self.F.yview)
        self.buttons = []
        
        self.cdir = os.getcwd()
        self.back()
     #   print(self.back())
   
    def back(self, dr = ""):
        if dr == "": dr = self.cdir
        self.cdir = dr[0:dr.rfind('\\')]
        self.show()
    
    def show(self):
        for i in self.buttons: i.destroy()
        
        
#        self.C.create_window((0,0), window=self.F, anchor='nw')
        for i in os.listdir(self.cdir):
            b = Button(self.F, text=i, command = partial(self.moveto, self.cdir + "\\" + i))
            self.buttons.append(b)
            b.pack(anchor = "nw")
        b = Button(self.F, text="back", command=partial(self.back, self.cdir))
        self.buttons.append(b)
        b.pack(anchor = "nw")
        self.F.pack(side = LEFT, fill=BOTH)

        
        
        
     #   self.F.pack(side = LEFT, fill = BOTH)
        

    def moveto(self, val):
        if os.path.isdir(val):
            self.cdir = val
            self.show()
        else:
            self.parser.add(val)
          
            
