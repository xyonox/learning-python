from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk

root = Tk()

file_path = None

def on_closing():
    save()
    print("byeeeeeee")
    root.destroy()

def save():
    global file_path
    print(file_path)
    if file_path is None:
        print("hey")
        fp = filedialog.asksaveasfilename(defaultextension=".txt",
                                          filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")])

        if fp:
            file_path = fp
            print(textfeld.get("1.0", 'end-1c'))
            with open(file_path, "w") as f:
                f.write(textfeld.get("1.0", 'end-1c'))
    else:
        with open(file_path, "w") as f:
            f.write(textfeld.get("1.0", 'end-1c'))

def create_file():
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")])
    if file_path:
        textfeld.delete("1.0", 'end')
        root.title(file_path)

def on_key_event(event):
    global file_path
    if (event.state & 0x8) and event.keysym == 'l':
        file_path = filedialog.askopenfilename()
        print("Selected file:", file_path)

        if file_path:
            with open(file_path, "r") as f:
                textfeld.delete("1.0", 'end')
                textfeld.insert("1.0", f.read())
                root.title(file_path)
    elif (event.state & 0x8) and event.keysym == 's':
        save()
    elif (event.state & 0x8) and event.keysym == 'c':
        create_file()

if __name__ == "__main__":
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.geometry("500x400")

    root.bind('<KeyPress>', on_key_event)

    textfeld = tk.Text(root)
    textfeld.pack(expand=True, fill='both')

    root.mainloop()