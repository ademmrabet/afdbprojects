from tkinter import *
from tkinter.ttk import *

window = Tk() #Desktop window setup

window.title("AFDB Project") #naming the desktop window (title)
window.geometry('350x200') #dektop window geometry
welcome = Label(window, text = "Welcome to AFDB Project", font=("Arial Bold", 50)) #welcome message
welcome.grid(column=0, row=0) #welcome message lineup
txt = Entry(window, width = 10)#input text box
txt.grid(column=2, row = 0)

def clicked():
    res = "Welcome Mr/Mrs. "+ txt.get()
    welcome.configure(text = res)
btn = Button(window, text = "Click here", bg = "orange", fg = "red", command= clicked)
btn.grid(column=1, row=0)
window.mainloop()