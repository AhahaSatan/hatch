from tkinter import *
import random
from nim import Nim
ncols = 3
n = Nim(ncols)
F = Frame()
stv = StringVar(F)
stv.set("3")

d = [str(i) for i in range(1, 11)]
numselector = OptionMenu(F, stv, *d)
c = Canvas(F, width = (ncols)*100, height = 400)
F.pack()
c.grid()

def changepiles(*args):
    global ncols
    ncols = int(stv.get())
    if not locked:
        newgame()
stv.trace_add('write', changepiles)

def newgame():
    global n, rects, coords, locked
    n = Nim(ncols)
    c.delete("all")
    c.config(width = (ncols)*100)
    numselector.grid(row=2)
    rects = [[] for i in range(ncols)]
    coords = [[] for i in range(ncols)]
    for i in range(ncols):
        for j in range(n.piles[i]):
            topy = 400-(j+1)*15
            coords[i].append(topy)
            r = c.create_rectangle(i*100+20, topy, i*100+80, topy+15, fill = "green")
            rects[i].append(r)
    locked = False
def gameover():
    r.destroy()
    newgame()
def endgame(message):
    global r
    r = Tk()
    r.protocol("WM_DELETE_WINDOW", gameover)
    Label(r, text=message).pack()
def cpumove():
    global locked
    ccol = n.bestmove()
    for i in range(ccol[1], n.piles[ccol[0]]):
        c.itemconfig(rects[ccol[0]][i], fill='blue')
    n.move(ccol[0], ccol[1])
    if sum(n.piles)==0:
        endgame("The computer wins!")
    locked = False
    
def move(event):
    global locked, n
    if locked: return
    else:
        locked = True
        col = event.x//100
        if coords[col][n.piles[col]-1]>event.y:
            locked = False
            return
        for i in range(n.piles[col]-1, -1, -1):
            if coords[col][i]>event.y:
                n.move(col, i+1)
                break
            c.itemconfig(rects[col][i], fill='red')
        else:
            n.move(col, 0)
        if sum(n.piles)==0:
            endgame("You win!")
            return
        else:
            c.after(200, cpumove)
        


c.bind("<Button-1>", move)
newgame()
mainloop()
