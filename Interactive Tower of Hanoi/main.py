from tkinter import *
import time
from gamescreen import Gamescreen
from modelgame import Modelgame
disknumber = 5
paused = False
events = []
delay = 0
def hanoi(start, target, aux, size):
    if size == 0: return []
    global cp
    cc = cp.get_index(size)
    #print(cc)
    if cc == start:
        tt = hanoi(start, aux, target, size-1)
        tt.append([start, target])
        cp.move(start, target)
        return tt + hanoi(aux, target, start, size-1)
    elif cc == target:
        return hanoi(start, target, aux, size-1)
    else:
        tt = hanoi(aux, start, target, size-1)
        tt.append([aux, target])
        cp.move(aux, target)
        return tt + hanoi(start, target, aux, size-1)

def unpause():
    global paused
    global g
    global events
    paused = False
    g.unpause()
    events[:] = []
    
def cpumove():
    global paused
    global g, cp
    if paused: return
    paused = True
    g.C.delete(g.selected)
    g.pause()
    cp = Modelgame(g)
    global disknumber
    
    l = hanoi(0, 2, 1, disknumber)
    for i in range(len(l)):
        events.append(g.C.after(500*i, g.move, l[i][0], l[i][1]))
    g.C.after(500*len(l), unpause)
    
def update_e(n):
    global e
    e.delete(0, len(e.get()))
    e.insert(0, str(n))
def newgame():
    global e
    global disknumber, paused, g
    if paused:
        for i in events: g.C.after_cancel(i)
        unpause()
    try:
        disknumber = int(e.get())
        if disknumber > 13:
            disknumber = 13
            update_e(13)
        elif disknumber < 2:
            disknumber = 2
            update_e(2)
    except ValueError:
        disknumber = 5
        update_e(5)
    g.reset(disknumber)
frame = Frame()
g = Gamescreen(frame, disknumber)
cp = Modelgame(g)
e = Entry(frame, width="5")
e.insert(0, "5")
l1 = Label(frame, text = "Number of Disks:")
movebutton = Button(frame, text="Solution", command=cpumove)
newbutton = Button(frame, text="New Game", command=newgame)
movebutton.pack()
newbutton.pack()
l1.pack(side = LEFT)
e.pack(side = LEFT)

frame.pack()

mainloop()
