from matrix import Matrix
from tkinter import *
r = Frame()
r.pack()
f = Frame(r, bd = 3, background = "black")
f.pack(side = TOP)
entries = []
coord = []
for k in range(3):
    for l in range(3):
        tmpf = Frame(f, bd = 2, background = "black")
        tmpf.grid(row=k, column = l)
        for i in range(3):
            for j in range(3):
                e = Entry(tmpf, width = 3, justify = CENTER, font = ("Calibri", 20))
                e.grid(row=i, column=j, ipady = 6)
                entries.append(e)
                coord.append([k*3+i, l*3+j])
def solve():
    m = Matrix()
    inv = False
    for i in range(81):
        try:
            n = int(entries[i].get())
            if n>0 and n<10:
                try:
                    m.addnumber(coord[i][0], coord[i][1], n)
                except KeyError:
                    entries[i].delete(0, END)
                    inv = True
            else:
                entries[i].delete(0, END)
        except ValueError:
            entries[i].delete(0, END)
        if inv: break
    if not inv:
        a = m.solve()
        if not a:
            clearall()
        else:
            m.gensol()
            for i in range(81):
                entries[i].delete(0, END)
                entries[i].insert(0, m.sol[coord[i][0]][coord[i][1]])
    
            
def clearall():
    for i in entries:
        i.delete(0, END)
        
solvebutton = Button(r, text = "Solve", command = solve)
solvebutton.pack(side = BOTTOM)

clearbutton = Button(r, text = "Clear Board", command = clearall)
clearbutton.pack(side = BOTTOM)


mainloop()
