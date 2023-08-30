import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from text import Text

text = Text()

def select_file():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    f = fd.askopenfilename(title='Open a file',initialdir='/', filetypes=filetypes)
    clear_text()
    f = open(f)
    inputtxt.insert('1.0', f.read())    

def clear_text():
    inputtxt.delete("1.0", "end")
    
def Take_input():
    return inputtxt.get("1.0", "end-1c")
        
window = tk.Tk()
window.geometry("980x720")
window.title('TextToMusic')
window.resizable(False, False)
window.configure(bg="light grey")

label = tk.Label(window, text="Text to Music", font=('calibre',30, 'bold'), pady=50, bg="light grey")
label.pack(side = "top")

inputtxt = tk.Text(window, height = 10, width = 25, font=('calibre',12,),bg = "light yellow")
inputtxt.pack(fill="x", expand=True, padx=150)
inputtxt.insert(tk.INSERT, "Digite aqui...", )

button = tk.Button(window, text='Submit', font=('calibre',15, 'bold'), width=15, height=3, bg="grey", fg="light yellow", command = lambda:text.SetText(Take_input()))
button.pack(side="bottom", padx=15, pady=120)

open_button = ttk.Button(window, text='Open a File', command=select_file)

open_button.pack(expand=True)

window.mainloop()