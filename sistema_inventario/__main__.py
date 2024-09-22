from tkinter import *
import sistema_inventario.interfaz as GUI

if __name__ == "__main__":
    raiz = Tk()
    raiz.title("ACCESORIOS Y MANUALIDADES")
    raiz.resizable(False, False)
    raiz.config(bg="#ffe1c9", bd=20)
    app = GUI.GUI(raiz)
    raiz.mainloop()