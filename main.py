#Import Section
from sys import path
path.insert(0,"./module/")

import calc
from tkinter import *
from functools import partial

#Variables
Dictionary = {"+":calc.Add,"-":calc.Diff,"*":calc.Product,"/":calc.Div}
Buttons_num = dict()
Buttons_Oprs = dict()

Oprs = ["+", "-", "*", "/"]

Window_Size = "400x400"
Window_Title = "Calculator"

# Functions
def validate_only_digits(Key):
    return Key.isdigit() or Key == ''

def validate_only_opers(Key):
    return True if Key in ['+','-','/','*',''] else False

def Calc():
    Output_Area.config(state=NORMAL)
    Output_Area.delete('1.0', END)
    Operator = "+" if Input_Area_0.get() == '' else Input_Area_0.get()
    A = 0 if not Input_Area_1.get().isdigit() else int(Input_Area_1.get())
    B = 0 if not Input_Area_2.get().isdigit() else int(Input_Area_2.get())
    Output = str(Dictionary[Operator](A,B))
    Output_Area.insert(END, Output)
    Output_Area.config(state=DISABLED)

def Place(Val):
    try:
        Focus_Input = window.focus_get()
        Focus_Input.insert(END,Val)
    except Exception as Error:
        Focus_Input = Input_Area_1
        Focus_Input.insert(END, Val)

def Operator_Place(Opr):
    Input_Area_0.delete(0, END)
    Input_Area_0.insert(END, Opr)

def Create_Num_Buttons():
    tmp_x = 50
    tmp_y = 150
    button_width = 40
    button_height = 30

    for i in range(1, 10):
        Buttons_num[i] = Button(window, text=f"{i}", command=lambda i=i: Place(f"{i}"))
        Buttons_num[i].place(x=tmp_x, y=tmp_y, width=button_width, height=button_height)

        tmp_x += 50
        if i%3==0:
            tmp_y+=50
            tmp_x =50
    Buttons_num[0] = Button(window, text="0", command=lambda :Place("0"))
    Buttons_num[0].place(x=tmp_x + 50, y=tmp_y, width=button_width, height=button_height)

def Create_Oprs_Buttons():
    tmp_x = 230
    tmp_y = 200
    button_width = 30
    button_height = 40
    count = 0
    for o in Oprs:
        count += 1
        Buttons_Oprs[o] = Button(window, text=f"{o}", command=lambda o=o:Operator_Place(f"{o}"))
        Buttons_Oprs[o].place(x=tmp_x,y=tmp_y,width=button_width,height=button_height)
        tmp_x += 70
        if count % 2 == 0:
            tmp_y += 50
            tmp_x = 230
# Main
window = Tk()
window.geometry(Window_Size)
window.title(Window_Title)
window.resizable(False, False)

Input_Area_1 = Entry(window, validate='key', validatecommand=(window.register(validate_only_digits), '%P'))
Input_Area_1.insert(END, "0")
Input_Area_1.place(x=50, y=50,width=100, height=30)

Input_Area_0 = Entry(window, validate='key', validatecommand=(window.register(validate_only_opers), '%P'))
Input_Area_0.insert(END, "+")
Input_Area_0.place(x=170, y=50, width=30, height=30)

Input_Area_2 = Entry(window, validate='key', validatecommand=(window.register(validate_only_digits), '%P'))
Input_Area_2.insert(END, "0")
Input_Area_2.place(x=220, y=50,width=100, height=30)

Output_Area = Text(window, wrap='word', width=300, height=30)
Output_Area.insert(END, "0")
Output_Area.config(state=DISABLED)
Output_Area.place(x=50, y=100, width=280, height=30)

Calculate = Button(window,text="Calc", command=Calc)
Calculate.place(x=230, y=150, width=100, height=40)

window.bind("<Return>", lambda event: Calc())

Create_Num_Buttons()
Create_Oprs_Buttons()
window.mainloop()
