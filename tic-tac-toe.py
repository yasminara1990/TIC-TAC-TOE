#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 02:42:24 2021

@author: yasmin 
"""

from tkinter import *
import tkinter.messagebox as msg

window= Tk()
window.title('TIC-TAC-TOE')

digits = [1,2,3,4,5,6,7,8,9]
mark = '' 
count = 0
cells = ["cell"]*10

def win(cells,sign):
    return ((cells[1] == cells[2] == cells [3] == sign)
            or (cells[1] == cells[4] == cells [7] == sign)
            or (cells[1] == cells[5] == cells [9] == sign)
            or (cells[2] == cells[5] == cells [8] == sign)
            or (cells[3] == cells[6] == cells [9] == sign)
            or (cells[3] == cells[5] == cells [7] == sign)
            or (cells[4] == cells[5] == cells [6] == sign) 
            or (cells[7] == cells[8] == cells [9] == sign))

def checker(digit):
    global count, mark, digits
    if digit==1 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            cells[digit]=mark
        elif count%2!=0:
            mark = 'O'
            cells[digit]=mark
        button1.config(text = mark)
        count = count+1
        sign = mark
        if(win(cells,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            window.destroy()
        elif(win(cells,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            window.destroy()

    if digit==2 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            cells[digit]=mark
        elif count%2!=0:
            mark = 'O'
            cells[digit]=mark
        button2.config(text = mark)
        count = count+1
        sign = mark
        if(win(cells,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            window.destroy()
        elif(win(cells,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            window.destroy()

    if digit==3 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            cells[digit]=mark
        elif count%2!=0:
            mark = 'O'
            cells[digit]=mark
        button3.config(text = mark)
        count = count+1
        sign = mark
        if(win(cells,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            window.destroy()
        elif(win(cells,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            window.destroy()

    if digit==4 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            cells[digit]=mark
        elif count%2!=0:
            mark = 'O'
            cells[digit]=mark
        button4.config(text = mark)
        count = count+1
        sign = mark
        if(win(cells,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            window.destroy()
        elif(win(cells,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            window.destroy()

    if digit==5 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            cells[digit]=mark
        elif count%2!=0:
            mark = 'O'
            cells[digit]=mark
        button5.config(text = mark)
        count = count+1
        sign = mark
        if(win(cells,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            window.destroy()
        elif(win(cells,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            window.destroy()

    if digit==6 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            cells[digit]=mark
        elif count%2!=0:
            mark = 'O'
            cells[digit]=mark
        button6.config(text = mark)
        count = count+1
        sign 
    if(win(cells,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            window.destroy()
    elif(win(cells,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            window.destroy()

    if digit==7 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            cells[digit]=mark
        elif count%2!=0:
            mark = 'O'
            cells[digit]=mark
        button7.config(text = mark)
        count = count+1
        sign = mark
        if(win(cells,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            window.destroy()
        elif(win(cells,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            window.destroy()

    if digit==8 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            cells[digit]=mark
        elif count%2!=0:
            mark = 'O'
            cells[digit]=mark
        button8.config(text = mark)
        count = count+1
        sign = mark
        if(win(cells,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            window.destroy()
        elif(win(cells,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            window.destroy()

    if digit==9 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            cells[digit]=mark
        elif count%2!=0:
            mark = 'O'
            cells[digit]=mark
        button9.config(text = mark)
        count = count+1
        sign = mark
        if(win(cells,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            window.destroy()
        elif(win(cells,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            window.destroy()
  
    if(count>8 and win(cells,'X')==False and win(cells,'O')==False):
        msg.showinfo("Result","Match Tied")
        window.destroy()
        
Label(window,text="player1 : X",font="times 15").grid(row=0,column=1)
Label(window,text="player2 : O",font="times 15").grid(row=0,column=2)

button1=Button(window,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(1))
button1.grid(row=1,column=1)
button2=Button(window,width=15,height=7,font=('Times 16 bold'),command=lambda:checker(2))
button2.grid(row=1,column=2)

button3=Button(window,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(3))
button3.grid(row=1,column=3)
button4=Button(window,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(4))
button4.grid(row=2,column=1)

button5=Button(window,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(5))
button5.grid(row=2,column=2)
button6=Button(window,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(6))
button6.grid(row=2,column=3)

button7=Button(window,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(7))
button7.grid(row=3,column=1)
button8=Button(window,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(8))
button8.grid(row=3,column=2)

button9=Button(window,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(9))
button9.grid(row=3,column=3)


window.mainloop()