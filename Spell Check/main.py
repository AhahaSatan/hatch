#import time
from functools import partial
from spellchecker import Spellchecker
from tkinter import *

#time.clock()

spl = Spellchecker()
st = ["abyss", "abyse", "recomendations"]
f = Frame()
f.pack()
txt = Text(f)
finput = []
disabled = False
lb = Listbox()
lstr = []
def close(ind, curr):
    global disabled
    txt.tag_remove('sel', "1."+str(curr), "1."+str(curr+len(finput[ind])))
    root.destroy()
    checkfrom(ind+1, curr+len(finput[ind])+1)
    
def done(ind, curr):
    global lb, lstr
    tp = lb.curselection()
    txt.tag_remove('sel', "1."+str(curr), "1."+str(curr+len(finput[ind])))
    root.destroy()
    if len(tp)>0 and tp[0] < len(lstr):
        txt.config(state=NORMAL)
        txt.delete("1."+str(curr), "1."+str(curr+len(finput[ind])))
        txt.insert("1."+str(curr), lstr[tp[0]])
        txt.config(state=DISABLED)
        checkfrom(ind+1, curr+len(lstr[tp[0]])+1)
    
    else: checkfrom(ind+1, curr+len(finput[ind])+1)
    
    
def checkfrom(ind, curr):
    global disabled, root, lstr, lb
    for tpind in range(ind, len(finput)):
        tpi = finput[tpind]
        i=tpi
        st = 0
        ed = len(tpi)-1
        while st < len(tpi):
            if tpi[st].isalpha() or tpi[st].isdigit():
                break
            else: st+=1
        if st != len(tpi):
            while ed >= 0:
                if tpi[ed].isalpha() or tpi[ed].isdigit():
                    break
                else: ed-=1
            i = tpi[st:ed+1]
        if i.lower() not in spl.s:
            if i[0].isupper():lstr = [tpi[:st]+k[0].upper()+k[1:]+tpi[ed+1:] for k in spl.recommendations(i.lower())]
                
            else: lstr = [tpi[:st]+k+tpi[ed+1:] for k in spl.recommendations(i.lower())]
            txt.tag_add('sel', "1."+str(curr), "1."+str(curr+len(tpi)))
            root = Tk()
            lb = Listbox(root, selectmode="SINGLE")
            dn = Button(root, text="Done", command = partial(done,tpind, curr))
            root.protocol("WM_DELETE_WINDOW", partial(close, tpind, curr))
            for k in lstr:
                lb.insert(END, k)
            if len(lstr)==0: lb.insert(END, "No matches found")
            else: lb.insert(END, "None of the above")
            

            lb.pack()
            dn.pack()
            return
        curr += len(tpi)+1
    disabled = False
    txt.config(state=NORMAL)
    
def checktext():
    
    global finput, disabled
    if disabled:
        return
    disabled = True
    
    finput = txt.get("1.0", "end-1c").split()
    txt.delete("1.0", END)
    txt.insert(END, " ".join(finput))
    txt.config(state=DISABLED)
    checkfrom(0, 0)
    
        

checkbutton = Button(f, command = checktext, text = "Check Text")
txt.pack()
checkbutton.pack()
mainloop()
