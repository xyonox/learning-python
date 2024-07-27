
from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk

root = Tk()

file_path = ""

def on_closing():
    save()
    print("byeeeeeee")
    root.destroy()

def save():
    if file_path == "":
        fp = filedialog.askopenfilename()

        print(textfeld.get("1.0", 'end-1c'))
        with open(fp, "w") as f:

            f.write(textfeld.get("1.0", 'end-1c'))
    else:
        with open(file_path, "w") as f:
            f.write(textfeld.get("1.0", 'end-1c'))

def on_key_event(event):
    if (event.state & 0x8) and event.keysym == 'l':
        file_path = filedialog.askopenfilename()
        print("Selected file:", file_path)

        with open(file_path, "r") as f:
            textfeld.delete("1.0", 'end')
            textfeld.insert("1.0" ,f.read())
    elif (event.state & 0x8) and event.keysym == 's':
        save()

if __name__ == "__main__":
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.geometry("400x300")

    root.bind('<KeyPress>', on_key_event)

    textfeld = tk.Text(root)
    textfeld.pack(expand=True, fill='both')

    root.mainloop()
