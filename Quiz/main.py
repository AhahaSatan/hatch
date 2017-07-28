import tkinter as tk
import requests
from questions import Questions
import html
F = tk.Frame()
F.pack()
stv = tk.StringVar(F)
stv.set("All")
cats = requests.get("https://opentdb.com/api_category.php").json()['trivia_categories']
d = {i["name"]:i["id"] for i in cats}
d["All"]=None
selector = tk.OptionMenu(F, stv, *d)
l = tk.Label(F, text = "Choose a category:")
l.grid()
selector.grid(row=0, column=1)
counter = tk.Label(F, text = "Correct: 0   Incorrect: 0")
counter.grid()
changed = True
def display():
    global stv, changed
    question['correct_answer'] = html.unescape(question['correct_answer'])
    answers = [html.unescape(i) for i in question['incorrect_answers']]
    answers.append(question['correct_answer'])
    answers.sort()
    
    selector['menu'].delete(0, 'end')
    changed = False
    stv.set(answers[0])
    changed = True
    for i in answers:
        selector['menu'].add_command(label=i, command=tk._setit(stv, i))
    
    l.config(text=html.unescape(question['question']))
def answer(*args):
    if not changed: return
    global question
    right = qlist.answer(stv.get(), question)
    if not right:
        r = tk.Tk()
        l = tk.Label(r, text = "Wrong! Correct answer was: "+question['correct_answer'])
        l.pack()
    counter.config(text = "Correct: "+str(qlist.totalcorrect)+"   Incorrect: "+str(qlist.totalwrong))
    question = qlist.next()
    display()
def pickcategory(*args):
    global catid, qlist, question, stv, selector
    catid = d[stv.get()]
    qlist = Questions(catid)
    question = qlist.next()
    
    stv = ""
    selector.destroy()
    stv = tk.StringVar(F)
    stv.trace("w", answer)
    selector = tk.OptionMenu(F, stv, "")
    selector.grid(row=0, column=1)
    display()
    

stv.trace("w", pickcategory)
tk.mainloop()
