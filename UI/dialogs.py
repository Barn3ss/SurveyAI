from tkinter import messagebox
def info(titulo,texto):
    messagebox.showinfo(titulo,texto)

def warning(titulo,texto):
    messagebox.showwarning(titulo,texto)

def error(titulo,texto):
    messagebox.showerror(titulo,texto)

def confirmar(titulo,texto):
    return messagebox.askyesno(titulo,texto)
