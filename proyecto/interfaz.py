from inventario import Inventario
from producto import Producto
#se importa messagebox de tkinter para que abra una ventana emergente para mostrar informacion o un error de validación
from tkinter import messagebox
from tkinter import *
import datetime

#Se crea una clase para crear los atributos, widgets del tkinter y los comandos pertinentes
class GUI:
    def __init__(self, root):
        self.root = root
        self.inventario = Inventario()  # Instanciar el inventario
        self.create_widgets()

    def create_widgets(self):
        self.tituloframe = Frame(self.root)
        self.tituloframe.grid(row=0, column=0)
        self.tituloframe.config(bg="#afc7b9", bd=3, relief="ridge")

        self.botonEntrada = Button(self.tituloframe, text="Registrar entrada", command=self.registrar_entrada)
        self.botonEntrada.grid(row=0, column=0, padx=10)
        self.botonSalida = Button(self.tituloframe, text="Registrar Salida", command=self.registrar_salida)
        self.botonSalida.grid(row=0, column=1, padx=10)
        self.botonInventario = Button(self.tituloframe, text="Obtener inventario", command=self.mostrar_inventario2)
        self.botonInventario.grid(row=0, column=2, padx=10)
        self.botonSalir = Button(self.tituloframe, text="Salir", command=self.salida)
        self.botonSalir.grid(row=0, column=3, padx=10)

    def registrar_entrada(self):
        self.entradaframe = Frame(self.root, bg="#afc7b9", bd=3, relief="ridge")
        self.entradaframe.grid(row=1, column=0, padx=10, pady=10)
        self.entradaframe.config(width="450", height="200")
        self.entradaframe.grid_propagate(False)

        Label(self.entradaframe, text="Nombre del Producto:", fg="#998b82", bg="#afc7b9", font=(15)).grid(row=0, column=0)
        self.cuadroNombre = Entry(self.entradaframe)
        self.cuadroNombre.grid(row=0, column=1)
        Label(self.entradaframe, text="Precio del Producto:", fg="#998b82", bg="#afc7b9", font=(15)).grid(row=1, column=0)
        self.cuadroPrecio = Entry(self.entradaframe)
        self.cuadroPrecio.grid(row=1, column=1)
        Label(self.entradaframe, text="Cantidad a ingresar:", fg="#998b82", bg="#afc7b9", font=(15)).grid(row=2, column=0)
        self.cuadroCantidad = Entry(self.entradaframe)
        self.cuadroCantidad.grid(row=2, column=1)

        Button(self.entradaframe, text="Volver", command=self.volver).grid(row=3, column=0, padx=10)
        Button(self.entradaframe, text="Enviar", command=self.enviar_entrada).grid(row=3, column=1, padx=10)

    def enviar_entrada(self):
        nombre = self.cuadroNombre.get()
        
        try:
            precio = float(self.cuadroPrecio.get())
            cantidad = int(self.cuadroCantidad.get())
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser números válidos")
            return
        
        tiempo = datetime.datetime.now().strftime('%d-%m-%Y/%H:%M:%S')
        producto = Producto(nombre, precio, cantidad, tiempo)
        self.inventario.registrar_entrada(producto, cantidad)
        messagebox.showinfo("Registro de entrada", f"{producto.nombre} x{cantidad} - {producto.tiempo}")
        self.volver()


    def registrar_salida(self):
        self.entradaframe = Frame(self.root, bg="#fca89d", bd=3, relief="ridge")
        self.entradaframe.grid(row=1, column=0, padx=10, pady=10)
        self.entradaframe.config(width="450", height="150")
        self.entradaframe.grid_propagate(False)

        Label(self.entradaframe, text="Nombre del Producto:", fg="#998b82", bg="#fca89d", font=(15)).grid(row=0, column=0)
        self.cuadroNombreSalida = Entry(self.entradaframe)
        self.cuadroNombreSalida.grid(row=0, column=1)
        Label(self.entradaframe, text="Cantidad a registrar:", fg="#998b82", bg="#fca89d", font=(15)).grid(row=1, column=0)
        self.cuadroCantidadSalida = Entry(self.entradaframe)
        self.cuadroCantidadSalida.grid(row=1, column=1)

        Button(self.entradaframe, text="Volver", command=self.volver).grid(row=2, column=0, padx=10)
        Button(self.entradaframe, text="Enviar", command=self.enviar_salida).grid(row=2, column=1, padx=10)

    def enviar_salida(self):
        nombre = self.cuadroNombreSalida.get()
        try:
            cantidad = int(self.cuadroCantidadSalida.get())
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número válido")
            return

        producto = next((p for p in self.inventario.productos if p.nombre == nombre), None)
        if producto:
            self.inventario.registrar_salida(producto, cantidad)
        else:
            messagebox.showerror("Error", "Producto no encontrado")
        self.volver()

    def mostrar_inventario(self):
        inventario_info = ""
        for p in self.inventario.productos:
            inventario_info += f"Nombre {p.nombre}: cantidad: {p.cantidad} x ${p.precio} {p.tiempo}\n"
        if not inventario_info:
            inventario_info = "El inventario está vacío."
        messagebox.showinfo("Inventario", inventario_info)
    def mostrar_inventario2(self):
        self.entradaframe = Frame(self.root, bg="#fca89d", bd=3, relief="ridge")
        self.entradaframe.grid(row=1, column=0, padx=10, pady=10)
        #self.entradaframe.config(width="450", height="150")
        self.entradaframe.grid_propagate(False)

        nombre= Entry(self.entradaframe, width=10)
        nombre.grid(row=0, column=0)
        nombre.insert(0, 'Nombre')
        cantidad = Entry(self.entradaframe, width=10)
        cantidad.grid(row=0, column=1)
        cantidad.insert(0, 'Cantidad')
        precio = Entry(self.entradaframe, width=10)
        precio.grid(row=0, column=2)
        precio.insert(0, 'Precio')
        tiempo = Entry(self.entradaframe, width=20)
        tiempo.grid(row=0, column=3)
        tiempo.insert(0, 'Fecha y Hora')
        for i,p in enumerate(self.inventario.productos):
            n = Entry(self.entradaframe, width=10)
            n.grid(row=i+1, column=0)
            n.insert(0, f"{p.nombre}")
            c = Entry(self.entradaframe, width=10)
            c.grid(row=i+1, column=1)
            c.insert(0, f"{p.cantidad}")
            pe = Entry(self.entradaframe, width=10)
            pe.grid(row=i+1, column=2)
            pe.insert(0, f"${p.precio}")
            t = Entry(self.entradaframe, width=20)
            t.grid(row=i+1, column=3)
            t.insert(0, f"{p.tiempo}")
        Button(self.entradaframe, text="Volver", command=self.volver).grid(row=i+3, column=0, padx=10)


    def salida(self):
        self.root.destroy()

    def volver(self):
        for widget in self.root.winfo_children():
            widget.grid_forget()
        self.create_widgets()

if __name__ == "__main__":
    raiz = Tk()
    raiz.title("ACCESORIOS Y MANUALIDADES")
    raiz.resizable(False, False)
    raiz.config(bg="#ffe1c9", bd=20)
    app = GUI(raiz)
    raiz.mainloop()

