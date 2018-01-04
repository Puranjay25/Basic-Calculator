import tkinter as tk
from operator import add
import pygame

pygame.init()
sound=pygame.mixer.Sound("Button-click-sound.mp3")

window=tk.Tk()
window.title("My Calculator 1.0")
window.geometry("600x600")
text=[]

frame1=tk.Frame(window)
frame1.pack(side=tk.TOP)

main_label=tk.Label(frame1,text="A Basic Calculator",font=("Courier",20),bg="cyan")
main_label.pack(side=tk.LEFT)

frame2=tk.Frame(window)
frame2.pack(side=tk.TOP)

text_screen=tk.Text(frame2,font="Arial",height=2)
text_screen.pack(side=tk.LEFT)

def show_text(a):
    text.append(a)
    sound.play()
    text_screen.insert(tk.END,a)
    
def clean_area():
    text_screen.delete(1.0,tk.END)
    
def find_number(p):
    k=len(p)
    number=0
    l1=0
    l2=-1
    if p.count('.')==1:
        k=p.index('.')
    start=k-1
    while 1:
        number+=(p[start]*(10**l1))
        start-=1
        l1+=1
        if start<0:
            break
    if k!=len(p):
        start=k+1
        while 1:
            number+=(p[start]*(10**l2))
            l2-=1
            start+=1
            if start==len(p):
                break
    return number
    
def solve():
    number1_list=[]
    number2_list=[]
    if text.count('+')==1:
        index=text.index('+')
    elif text.count('-')==1:
         index=text.index('-')
    elif text.count('*')==1:
         index=text.index('*')
    elif text.count('/')==1:
         index=text.index('/')
    elif text.count('^')==1:
        index=text.index('^')
           
    for i in range(index):
        number1_list.append(text[i])
    
    for j in range(index+1,len(text)):
        number2_list.append(text[j])
        
    number1=find_number(number1_list)
    number2=find_number(number2_list)    
    text_screen.delete(1.0,tk.END)
    if text[index]=='+':
        text_screen.insert(tk.END,number1+number2)
    elif text[index]=='-':
        text_screen.insert(tk.END,number1-number2)
    elif text[index]=='*':
        text_screen.insert(tk.END,number1*number2)
    elif text[index]=='/':
        text_screen.index(tk.END,number1/number2)
    elif text[index]=='^':
        text_screen.insert(tk.END,number1**number2)

#BUTTONS
frame3=tk.Frame(window)
frame3.pack(side=tk.TOP)

button9=tk.Button(frame3,text="9",font="Arial",activebackground="darkslateblue",command=lambda:show_text(9),bd=7,width=10)
button9.pack(side=tk.LEFT)

button8=tk.Button(frame3,text="8",font="Arial",activebackground="darkslateblue",command=lambda:show_text(8),bd=7,width=10)
button8.pack(side=tk.LEFT)

button7=tk.Button(frame3,text="7",font="Arial",activebackground="darkslateblue",command=lambda:show_text(7),bd=7,width=10)
button7.pack(side=tk.LEFT)

frame4=tk.Frame(window)
frame4.pack(side=tk.TOP)

button6=tk.Button(frame4,text="6",font="Arial",activebackground="darkslateblue",command=lambda:show_text(6),bd=7,width=10)
button6.pack(side=tk.LEFT)

button5=tk.Button(frame4,text="5",font="Arial",activebackground="darkslateblue",command=lambda:show_text(5),bd=7,width=10)
button5.pack(side=tk.LEFT)

button4=tk.Button(frame4,text="4",font="Arial",activebackground="darkslateblue",command=lambda:show_text(4),bd=7,width=10)
button4.pack(side=tk.LEFT)

frame5=tk.Frame(window)
frame5.pack(side=tk.TOP)

button3=tk.Button(frame5,text="3",font="Arial",activebackground="darkslateblue",command=lambda:show_text(3),bd=7,width=10)
button3.pack(side=tk.LEFT)

button2=tk.Button(frame5,text="2",font="Arial",activebackground="darkslateblue",command=lambda:show_text(2),bd=7,width=10)
button2.pack(side=tk.LEFT)

button1=tk.Button(frame5,text="1",font="Arial",activebackground="darkslateblue",command=lambda:show_text(1),bd=7,width=10)
button1.pack(side=tk.LEFT)

frame6=tk.Frame(window)
frame6.pack(side=tk.TOP)

button_clr=tk.Button(frame6,text="CLR",font="Arial",activebackground="red",width=10,command=clean_area,bd=12)
button_clr.pack(side=tk.LEFT)

button0=tk.Button(frame6,text="0",font="Arial",activebackground="darkslateblue",command=lambda:show_text(0),bd=7,width=10)
button0.pack(side=tk.LEFT)

button_point=tk.Button(frame6,text=".",font="Arial",activebackground="darkslateblue",command=lambda:show_text("."),bd=7,width=10)
button_point.pack(side=tk.LEFT)

button_plus=tk.Button(frame3,text="+",font="Arial",activebackground="darkslateblue",command=lambda:show_text("+"),bd=10,width=10)
button_plus.pack(side=tk.LEFT)

button_minus=tk.Button(frame4,text="-",font="Arial",activebackground="darkslateblue",command=lambda:show_text("-"),bd=10,width=10)
button_minus.pack(side=tk.LEFT)

button_multiply=tk.Button(frame5,text="*",font="Arial",activebackground="darkslateblue",command=lambda:show_text("*"),bd=10,width=10)
button_multiply.pack(side=tk.LEFT)

button_divide=tk.Button(frame6,text="/",font="Arial",activebackground="darkslateblue",command=lambda:show_text("/"),bd=10,width=10)
button_divide.pack(side=tk.LEFT)

frame7=tk.Frame(window)
frame7.pack(side=tk.TOP)

button_equal=tk.Button(frame7,text="=",activebackground="green",font="Arial",command=solve,bd=12,width=10)
button_equal.pack(side=tk.LEFT)

button_power=tk.Button(frame7,font="Aria",text="^",bd=10,width=10,activebackground="darkslateblue",command=lambda:show_text("^"))
button_power.pack(side=tk.LEFT)


window.mainloop()