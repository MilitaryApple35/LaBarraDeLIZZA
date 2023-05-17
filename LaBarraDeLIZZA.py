import tkinter as tk
import ctypes
from gui import frame, barra_menu
import threading

def main():
    root=tk.Tk()
    root.title("La Barra de LIZZA")
    root.iconbitmap("images/IcoBarraLIZZA.ico")
    root.resizable(True, True)
    barra_menu(root)
    app=frame(root= root)
    app.mainloop()

if __name__== '__main__':
    main()