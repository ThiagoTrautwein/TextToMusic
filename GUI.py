import tkinter as tk

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
        
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

button = tk.Button(window, text='Submit', font=('calibre',15, 'bold'), width=15, height=3, bg="grey", fg="light yellow",command = lambda:Take_input())
button.pack(side="bottom", padx=15, pady=120)

window.mainloop()