from tkinter import *
from tkinter import ttk
root = Tk()

root.title("My First Gui")
root.geometry("500x500")

def on_closing():
    print("byeeeeeee")
    root.destroy()

def submit():
    lab.config(text=en.get())
    en.delete(0, 'end')
def submit2():
    lab2.config(text=tt.get("1.0", 'end-1c'))
    tt.delete("1.0", 'end')

root.protocol("WM_DELETE_WINDOW", on_closing)

lab = Label(root, text='hey')
lab.pack()
lab.config(text='ni na nu')



en = Entry(root)
en.pack()


b = Button(text="submit", command=submit)
b.pack()

lab2 = Label(text="")
lab2.pack()
tt = Text(root, width=40, height=10)
tt.pack()

b2 = Button(text="submit", command=submit2)
b2.pack()


root.mainloop()