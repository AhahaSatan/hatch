from tkinter import *
from chain import Chain
class Display:
    def __init__(self):
        self.chain = Chain()
        self.C = Canvas()
        self.e = Entry(self.C)
        self.l = Label(self.C, text = "File name:")
        self.addbutton = Button(self.C, text = "Add file", command = self.addfile)
        self.genbutton = Button(self.C, text = "Generate", command = self.generate)
        self.T = Text(self.C)
        self.C.pack()
        self.l.pack(side = LEFT)
        self.e.pack(side = LEFT)
        self.addbutton.pack(side = LEFT)
        self.genbutton.pack()
        self.T.pack()
        mainloop()

    def addfile(self):
        self.chain.addfile(self.e.get())

    def generate(self):
        self.T.insert(END, self.chain.makeline())
