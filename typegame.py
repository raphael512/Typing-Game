from tkinter import *
from hehe import words
from word import word
from tkinter import messagebox
import random
import time

def newWord():
    if(w1.getActive() == False):
        w1.setWord(words[random.randint(0, 466394)])
        w1.setActive(True)
        w1.setCount(0)
        w1.setY(0)
        lbl1['text'] = w1.getWord()
    elif(w2.getActive() == False):
        w2.setWord(words[random.randint(0, 466394)])
        w2.setActive(True)
        w2.setCount(0)
        w2.setY(0)
        lbl2['text'] = w2.getWord()
    elif(w3.getActive() == False):
        w3.setWord(words[random.randint(0, 466394)])
        w3.setActive(True)
        w3.setCount(0)
        w3.setY(0)
        lbl3['text'] = w3.getWord()
    elif(w4.getActive() == False):
        w4.setWord(words[random.randint(0, 466394)])
        w4.setActive(True)
        w4.setCount(0)
        w4.setY(0)
        lbl4['text'] = w4.getWord()
    elif(w5.getActive() == False):
        w5.setWord(words[random.randint(0, 466394)])
        w5.setActive(True)
        w5.setCount(0)
        w5.setY(0)
        lbl5['text'] = w5.getWord()

def check(text):
    global score
    if(text == w1.getWord()):
        score += 100
        w1.setActive(False)
        root.after(1500, newWord)
        entry.delete(0, END)
        lbl1.place_forget()
    elif(text == w2.getWord()):
        score += 100
        w2.setActive(False)
        root.after(1500, newWord)
        entry.delete(0, END)
        lbl2.place_forget()
    elif(text == w3.getWord()):
        score += 100
        w3.setActive(False)
        root.after(1500, newWord)
        entry.delete(0, END)
        lbl3.place_forget()
    elif(text == w4.getWord()):
        score += 100
        w4.setActive(False)
        root.after(1500, newWord)
        entry.delete(0, END)
        lbl4.place_forget()
    elif(text == w5.getWord()):
        score += 100 
        w5.setActive(False)
        root.after(1500, newWord)
        entry.delete(0, END)
        lbl5.place_forget()
    print(score)

def wewz(self):
    entry.delete(0, END)

root = Tk()
root.title("Typing Game")
root.geometry("800x800")

count = 0
life = 3
global score
score = 0
speed = 7
txt = StringVar()

w1 = word(words[random.randint(0, 466394)])
w2 = word(words[random.randint(0, 466394)])
w3 = word(words[random.randint(0, 466394)])
w4 = word(words[random.randint(0, 466394)])
w5 = word(words[random.randint(0, 466394)])

x1 = w1.getWord()
x2 = w2.getWord()
x3 = w3.getWord()
x4 = w4.getWord()
x5 = w5.getWord()

entry = Entry(root, textvariable = txt, width = 30, borderwidth = 1, relief = "solid")
entry.place(x = 335, y = 700)
root.bind("<Return>", wewz)

lbl1 = Label(root, borderwidth = 1, relief = "solid", text = x1)
lbl2 = Label(root, borderwidth = 1, relief = "solid", text = x2)
lbl3 = Label(root, borderwidth = 1, relief = "solid", text = x3)
lbl4 = Label(root, borderwidth = 1, relief = "solid", text = x4)
lbl5 = Label(root, borderwidth = 1, relief = "solid", text = x5)

scoreLabel = Label(root, borderwidth = 1, relief = "solid", text = "Score: {}".format(score))
scoreLabel.configure(font=("Sans Serif", 24))
scoreLabel.place(x = 620, y = 10)

lbl1.config(font=("Sans Serif", 28))
lbl2.config(font=("Sans Serif", 28))
lbl3.config(font=("Sans Serif", 28))
lbl4.config(font=("Sans Serif", 28))
lbl5.config(font=("Sans Serif", 28))

w1.setActive(True)
root.after(1500, newWord)
root.after(3000, newWord)
root.after(4500, newWord)
root.after(6000, newWord)
root.after(7500, newWord)

while True:
    if(w1.getActive() == True):
        temp = w1.getCount()
        lbl1.place(x = w1.getX(), y = w1.getY() + temp)
        w1.setCount(temp + speed)
        if(w1.getCount() > 800):
            life -= 1
            w1.setActive(False)
            root.after(1500, newWord)

    if(w2.getActive() == True):
        temp = w2.getCount()
        lbl2.place(x = w2.getX(), y = w2.getY() + temp)
        w2.setCount(temp + speed)
        if(w2.getCount() > 800):
            life -= 1
            w2.setActive(False)
            root.after(1500, newWord)

    if(w3.getActive() == True):
        temp = w3.getCount()
        lbl3.place(x = w3.getX(), y = w3.getY() + temp)
        w3.setCount(temp + speed)
        if(w3.getCount() > 800):
            print(w3.getCount())
            life -= 1
            w3.setActive(False)
            root.after(1500, newWord)

    if(w4.getActive() == True):
        temp = w4.getCount()
        lbl4.place(x = w4.getX(), y = w4.getY() + temp)
        w4.setCount(temp + speed)
        if(w4.getCount() > 800):
            life -= 1
            w4.setActive(False)
            root.after(1500, newWord)

    if(w5.getActive() == True):
        temp = w5.getCount()
        lbl5.place(x = w5.getX(), y = w5.getY() + temp)
        w5.setCount(temp + speed)
        if(w5.getCount() > 800):
            life -= 1
            w5.setActive(False)
            root.after(1500, newWord)
   
    if(life == 0 or life < 0):
        messagebox.showinfo(title="./.", message="Talo ka lods")
        root.destroy()  
    check(entry.get())
    scoreLabel['text'] = "Score: {}".format(score)
    time.sleep(0.1)
    root.update()
    
root.mainloop()