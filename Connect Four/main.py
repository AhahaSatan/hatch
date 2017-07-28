from tkinter import *
from board import Board
from ai import Ai
from functools import partial

f = Frame()
f.pack()

a = Ai(4)
buttons = [[] for i in range(7)]
locked = False
emptyhash = 0
for i in range(7):
    for j in range(6):
        emptyhash^=a.hashvals[i][j][1]
b = Board([[] for i in range(7)], emptyhash)
def disp(message):
    global locked, r
    locked = True
    r = Tk()
    r.protocol("WM_DELETE_WINDOW", newgame)
    Label(r, text=message).pack()
    Button(r, text="Okay", command=newgame).pack()
def addpiece(column):
    global buttons, b, a, locked
    if len(b.board[column])==6 or locked:
        #print(b.board)
        return
    buttons[column][len(b.board[column])].config(bg = 'red')
    b.hash^=a.hashvals[column][len(b.board[column])][1]^a.hashvals[column][len(b.board[column])][2]
    b.board[column].append(1)
    if b.eval()== 9999998:
        disp("Player wins")
        return
    a.bestmove = -1
    a.negamax(b, 4, -9999999, 9999999, -1)
    buttons[a.bestmove][len(b.board[a.bestmove])].config(bg = 'yellow')
    b.hash^=a.hashvals[a.bestmove][len(b.board[a.bestmove])][0]^a.hashvals[a.bestmove][len(b.board[a.bestmove])][1]
    b.board[a.bestmove].append(-1)
    if b.eval()== -9999998:
        disp("Computer wins")
        return
    elif sum(len(i) for i in b.board)==42:
        disp("It's a tie")
        return

def newgame():
    global b, locked, r
    locked = False
    r.destroy()
    for i in buttons:
        for j in i:
            j.config(bg="white")
    b = Board([[] for i in range(7)], emptyhash)
    #print(b.board)
    
for i in range(7):
    for j in range(6):
        butt = Button(f, width = 10, height = 5, bg="white", command = partial(addpiece, i))
        butt.grid(row = 5-j, column = i)
        buttons[i].append(butt)

mainloop()
