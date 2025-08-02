from tkinter import *
root=Tk()

def my_click():
    mylabel=Label(root,text="Look ! I clicked a butten")
    mylabel.pack()

# by pad we can chang size of our butten
# by state we can enable or disable button
mybutten=Button(root,text="Click Me!",padx=5,pady=5,command=my_click,fg="blue",bg="Green" ) #stat=enable,state=disable
mybutten.pack()

root.mainloop()