# Import Section
from sys import path
path.insert(0,"./module/")

import calc
from tkinter import *

# Variables
Dictionary = {"+":calc.Add,"-":calc.Diff,"*":calc.Product,"/":calc.Div}
Buttons_num = dict()
Buttons_Oprs = dict()

Oprs = ["+", "-", "*", "/"]

Window_Size = "400x400"
Window_Title = "Calculator"

# Functions
def Validate(Key):
    if len(Key) == 0:
        return True
    if Key[-1].isdigit():
        return True
    elif Key[-1] in ['+', '-', '/', '*', '']:
        if Key[-2] not in ['+', '-', '/', '*']:
            return True
        else:
            return False
    else:
        return False

def Calc():
    Output_Area.config(state=NORMAL)
    Output_Area.delete('1.0', END)
    Raw_Input = Input_Area.get()
    if Raw_Input == "":
        Output = "None"
    else:
        Input = Raw_Input[1::] if Raw_Input[0] == '0' else Raw_Input
        Output = str(eval(Input))
    Output_Area.insert(END, Output)
    Output_Area.config(state=DISABLED)

def Place(Val):
    Input_Area.insert(END, Val)

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
        Buttons_Oprs[o] = Button(window, text=f"{o}", command=lambda o=o:Place(f"{o}"))
        Buttons_Oprs[o].place(x=tmp_x,y=tmp_y,width=button_width,height=button_height)
        tmp_x += 70
        if count % 2 == 0:
            tmp_y += 50
            tmp_x = 230

def Clear_All():
    Input_Area.delete(0, END)
    
    Output_Area.config(state=NORMAL)
    Output_Area.delete('1.0', END)
    Output_Area.config(state=DISABLED)

# Window and Widgets
window = Tk()
window.geometry(Window_Size)
window.title(Window_Title)
window.resizable(False, False)

Input_Area = Entry(window, validate='key', validatecommand=(window.register(Validate), '%P'))
Input_Area.insert(END, "0")
Input_Area.place(x=50, y=50, width=280, height=30)

Output_Area = Text(window, wrap='word', width=300, height=30)
Output_Area.config(state=DISABLED)
Output_Area.place(x=50, y=100, width=280, height=30)

Calculate = Button(window,text="Calc", command=Calc)
Calculate.place(x=230, y=150, width=100, height=40)

Clear = Button(window, text='CA', command=Clear_All)
Clear.place(x=230, y=300,width=50, height=40)

window.bind("<Return>", lambda event: Calc())

Create_Num_Buttons()
Create_Oprs_Buttons()

# mainloop
window.mainloop()
