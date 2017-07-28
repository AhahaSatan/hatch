import column
from tkinter import *

class Gamescreen:
    def __init__(self, frame, numcolumns):
        self.C = Canvas(frame, width=910, height=600)
        self.C.bind("<Button-1>", self.callback)
        self.l = []
        self.selected = None
        self.minimum_moves = None
        self.label = None
        self.winner = None
        self.set_vals(numcolumns)
        self.paused = False
        self.C.pack(side=TOP)
        
    def set_vals(self, numcolumns):
        self.movecounter = 0
        self.update_label()
        self.C.delete(self.winner)
        self.winner = None
        self.C.delete(self.minimum_moves)
        self.minimum_moves = self.C.create_text(155, 0, anchor = N, text = "Minimum Possible Moves: " + str(2**numcolumns - 1))
        tpl = [i for i in range(300, 59, -(240//(numcolumns-1)))]
        self.l.append(column.Column(155, [column.Disk(numcolumns-i, tpl[i]) for i in range(numcolumns)], self.C))
        for i in range(2): self.l.append(column.Column(455 + 300*i, [], self.C))
        self.clicked = False
        self.pvcolumn = 0

    def update_label(self):
        self.C.delete(self.label)
        self.label = self.C.create_text(355, 0, anchor = N, text = "Moves made: "+str(self.movecounter))
        
    def reset(self, numcolumns):
        while len(self.l) > 0:
            self.l[0].clear_all(self.C)
            del self.l[0]
        self.C.delete(self.selected)
        self.set_vals(numcolumns)

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False
        
    def move(self, oldc, newc):
        self.l[newc].add(self.l[oldc].remove(self.C), self.C)
        self.C.delete(self.label)
        self.movecounter += 1
        self.update_label()

    def callback(self, event):
        if self.paused: return
        cc = min(len(self.l)-1, event.x//300)
        if self.clicked:
            if cc!=self.pvcolumn and self.l[cc].can_add(self.l[self.pvcolumn]):
                self.move(self.pvcolumn, cc)
                if len(self.l[0].disks)==0 and len(self.l[1].disks)==0 and self.winner == None:
                    self.winner = self.C.create_text(655, 0, anchor = N, text = "You solved the puzzle! It took you " + str(self.movecounter) + " moves.")
                    
            self.clicked = False
            self.C.delete(self.selected)
        else:
            self.clicked = True
            self.pvcolumn = cc
            if len(self.l[cc].disks) > 0:
                self.selected = self.l[cc].display_disk(self.l[cc].disks[-1], self.C, len(self.l[cc].disks)-1, currfill="green")


