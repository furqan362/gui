from tkinter import *
root=Tk()
root.title("Simple calculator")
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def butten_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number) )
    
def butten_clear():
    e.delete(0,END)
    
def butten_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)
    
def butten_equal():
    second_number=e.get()
    e.delete(0,END)
    
    if math=="addition":
        e.insert(0,f_num + int(second_number))
    elif math=="subtraction":
        e.insert(0,f_num - int(second_number))
    elif math=="multiplication":
        e.insert(0,f_num * int(second_number))
    else:
        e.insert(0,f_num / int(second_number))

def butten_subtract():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0,END)
    

def butten_multiply():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)
    

def butten_divide():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0,END)
    
button_1=Button(root,text="1",padx=50,pady=25,command=lambda: butten_click(1))
button_2=Button(root,text="2",padx=50,pady=25,command=lambda: butten_click(2))
button_3=Button(root,text="3",padx=50,pady=25,command=lambda: butten_click(3))
button_4=Button(root,text="4",padx=50,pady=25,command=lambda: butten_click(4))
button_5=Button(root,text="5",padx=50,pady=25,command=lambda: butten_click(5))
button_6=Button(root,text="6",padx=50,pady=25,command=lambda: butten_click(6))
button_7=Button(root,text="7",padx=50,pady=25,command=lambda: butten_click(7))
button_8=Button(root,text="8",padx=50,pady=25,command=lambda: butten_click(8))
button_9=Button(root,text="9",padx=50,pady=25,command=lambda: butten_click(9))
button_0=Button(root,text="0",padx=50,pady=25,command=lambda: butten_click(0))
button_add=Button(root,text="+",padx=49,pady=20,command=butten_add)
button_equal=Button(root,text="=",padx=106,pady=20,command=butten_equal)
button_clear=Button(root,text="Clear",padx=98,pady=20,command=butten_clear)

button_subtract=Button(root,text="-",padx=50,pady=20,command=butten_subtract)
button_multiply=Button(root,text="*",padx=50,pady=20,command=butten_multiply)
button_divide=Button(root,text="/",padx=50,pady=20,command=butten_divide)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)


button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)
root.mainloop()