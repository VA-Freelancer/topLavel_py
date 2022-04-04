from tkinter import *



root = Tk()
root.geometry('400x300+800+300')  # размеры
root.title('TopLavel')  # Заголовок

def open_win():
    win = Toplevel()
    win.geometry("200x100+1000+400")
    win.overrideredirect(1)
    win.grab_set()
    l = Label(win, text="Hello Toplevel", bg="#000", fg="#fff").pack(expand=1, fill=BOTH)
    win.after(3000, lambda: win.destroy())

Button(root, text="Open", command=open_win, padx=40, pady=5).place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
