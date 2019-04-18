#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:59:56 2019

@author: ghadeerelmahdy
"""

import tkinter as tk
from tkinter import messagebox as mb
#Global Vairables
player=1 #switch between 1,2 
flag=1 #used to show if we finish game or not
windowshow = tk.Tk()
windowshow.title("Tik Tac Toe")
windowshow.geometry("400x300")
lbl1=tk.Label(windowshow,text="player1-> x ",bg="blue",font=("Times", "20", "bold italic"))
lbl1.grid(row=0,column=0)
lbl2=tk.Label(windowshow,text="player2-> o ",bg="red",font=("Times", "20", "bold italic"))
lbl2.grid(row=1,column=0) 
     

def window(player):
   mb.showinfo("windowshow", player+ " wins") 



def btn1Clicked():
 global player
 if (btn1['text'] == ""):
   if player ==1 :
     player = 2
     btn1["text"] = "X"
   else :
     player =1
     btn1["text"] = "O"
   #after updating our text, we should check if anyone wins  
   check()
   
def btn2Clicked():
 global player
 if btn2["text"] == "":
   if player ==1 :
     player = 2
     btn2["text"] = "X"
   else :
     player =1
     btn2["text"] = "O"
   #after updating our text, we should check if anyone wins  
   check() 
   
def btn3Clicked():
 global player
 if btn3["text"] == "":
   if player ==1 :
     player = 2
     btn3["text"] = "X"
   else :
     player =1
     btn3["text"] = "O"
   #after updating our text, we should check if anyone wins  
   check()        

def btn4Clicked():
 global player
 if btn4["text"] == "":
   if player ==1 :
     player = 2
     btn4["text"] = "X"
   else :
     player =1
     btn4["text"] = "O"
   #after updating our text, we should check if anyone wins  
   check() 
   
def btn5Clicked():
 global player
 if btn5["text"] == "":
   if player ==1 :
     player = 2
     btn5["text"] = "X"
   else :
     player =1
     btn5["text"] = "O"
   #after updating our text, we should check if anyone wins  
   check()
   
def btn6Clicked():
 global player
 if btn6["text"] == "":
   if player ==1 :
     player = 2
     btn6["text"] = "X"
   else :
     player =1
     btn6["text"] = "O"
   #after updating our text, we should check if anyone wins  
   check() 
   
def btn7Clicked():
 global player
 if btn7["text"] == "":
   if player ==1 :
     player = 2
     btn7["text"] = "X"
   else :
     player =1
     btn7["text"] = "O"
   #after updating our text, we should check if anyone wins  
   check()   
def btn8Clicked():
 global player
 if btn8["text"] == "":
   if player ==1 :
     player = 2
     btn8["text"] = "X"
   else :
     player =1
     btn8["text"] = "O"
   #after updating our text, we should check if anyone wins  
   check() 
   
def btn9Clicked():
 global player
 if btn9["text"] == "":
   if player ==1 :
     player = 2
     btn9["text"] = "X"
   else :
     player =1
     btn9["text"] = "O"
   #after updating our text, we should check if anyone wins  
   check() 

def restart():
 global player,flag   
 btn1["text"] = "" 
 btn2["text"] = "" 
 btn3["text"] = "" 
 btn4["text"] = "" 
 btn5["text"] = "" 
 btn6["text"] = ""
 btn7["text"] = "" 
 btn8["text"] = "" 
 btn9["text"] = ""      
 player=1
 flag=1 
 
def gridButton():
    btn1.grid(row=0,column=5)
    btn2.grid(row=0,column=6)
    btn3.grid(row=0,column=7)
    btn4.grid(row=1,column=5)
    btn5.grid(row=1,column=6)
    btn6.grid(row=1,column=7)
    btn7.grid(row=2,column=5)
    btn8.grid(row=2,column=6)
    btn9.grid(row=2,column=7)
    btnRestart.grid(row=2,column=9) 
   
btn1 = tk.Button(windowshow,text="",bg="blue",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn1Clicked)
btn2 = tk.Button(windowshow,text="",bg="blue",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn2Clicked)
btn3 = tk.Button(windowshow,text="",bg="blue",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn3Clicked)
btn4 = tk.Button(windowshow,text="",bg="blue",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn4Clicked)
btn5 = tk.Button(windowshow,text="",bg="blue",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn5Clicked)
btn6 = tk.Button(windowshow,text="",bg="blue",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn6Clicked)
btn7 = tk.Button(windowshow,text="",bg="blue",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn7Clicked)
btn8 = tk.Button(windowshow,text="",bg="blue",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn8Clicked)
btn9 = tk.Button(windowshow,text="",bg="blue",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn9Clicked)
btnRestart = tk.Button(windowshow,text="Restart",bg="blue",font=("Times", "15", "bold italic"),width=6,height=1,command=restart)
 

gridButton()


def check():
   global flag #for global action
   flag +=1
   if((btn1["text"]==btn2["text"]== btn3["text"]=="X" )or( btn1["text"]==btn2["text"]== btn3["text"]=="O")):
      window(btn1["text"]) 
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn4["text"]== btn5["text"]== btn6["text"]=="X" )or (btn4["text"]==btn5["text"]== btn6["text"]=="O")):
      window(btn4["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn7["text"]== btn8["text"]== btn9["text"]=="X" )or (btn7["text"]== btn8["text"]== btn9["text"]=="O")):
      window(btn7["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn1["text"]== btn4["text"]== btn7["text"]=="X" )or (btn1["text"]== btn4["text"]== btn7["text"]=="O")):
      window(btn1["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn2["text"]==btn5["text"]== btn8["text"]=="X" )or (btn2["text"]== btn5["text"]==btn8["text"]=="O")):
      window(btn2["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn3["text"]== btn6["text"]== btn9["text"]=="X") or( btn3["text"]== btn6["text"]== btn9["text"]=="O")):
      window(btn3["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn1["text"]== btn5["text"]==btn9["text"]=="X" )or (btn1["text"]==btn5["text"]==btn9["text"]=="O")):
      window(btn1["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn3["text"]== btn5["text"]== btn7["text"]=="X" )or( btn3["text"]== btn5["text"]==  btn7["text"]=="O")):
      window(btn3["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if flag ==10:
       mb.showinfo("windowshow", "End of the Game")  
       restart()
windowshow.mainloop()

