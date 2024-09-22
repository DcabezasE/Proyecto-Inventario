#Luego de inventario esta el modulo de interfaz grafica de usuario (GUI) y para eso se importa todo lo que hicimos anteriormente
from sistema_inventario.inventario import Inventario
from sistema_inventario.inventario import Producto
#Se importa todo de tkinter, tambien su messagebox para que abra una ventana emergente para mostrar informacion o un error de validación
from tkinter import messagebox
from tkinter import *
#Se importa el tiempo para su formato y el os(ya se sabra para que ;))
import datetime
import os

#Se crea una clase GUI para crear los atributos y las subclases que tendran todo
class GUI:
    #Se estructura:
    def __init__(self, root):
        self.root = root #La ventana base de tkinter
        self.inventario = Inventario()  #Se instancia el inventario
        self.create_widgets()#Y se manda a crear la pagina de inicio, por asi decirlo
    def create_widgets(self):
        self.tituloframe = Frame(self.root) #Se crea en la ventana (root) un recuadro en plano (frame) para añadir mas elementos
        self.tituloframe.grid(row=0, column=0) #El .grid sirve para posicionar en el root los elementos como en celdas o como matrices que inician en (0,0)
        self.tituloframe.config(bg="#afc7b9", bd=3, relief="ridge")#Se configura un color de fondo con el codigo rgb, con borde de 3 pixeles y con acabado de cresta, respectivamente
        #Se crea un boton (Button) sobre el frame, se le agrega nombre (text) y que hacer cuando se presiona (command)
        #Se posiciona con estilo .grid en el frame con espacio de 10 pixeles (pad) entre cada elemento de forma horizontal (x)
        self.botonEntrada = Button(self.tituloframe, text="Registrar entrada", command=self.ir_entrada) 
        self.botonEntrada.grid(row=0, column=0, padx=10)
        self.botonSalida = Button(self.tituloframe, text="Registrar Salida", command=self.ir_salida)
        self.botonSalida.grid(row=0, column=1, padx=10)
        self.botonInventario = Button(self.tituloframe, text="Obtener inventario", command=self.ir_inventario)
        self.botonInventario.grid(row=0, column=2, padx=10)
        self.botonSalir = Button(self.tituloframe, text="Salir", command=self.salida)
        self.botonSalir.grid(row=0, column=3, padx=10)  
    def volver(self):
        for widget in self.root.winfo_children(): #Consigue todo lo que hemos puesto en el root (winfo_children)
            widget.grid_forget() #lo borra de grid (grid_forget)
        self.create_widgets() #Y vuelve a crear la pagina de inicio
    def salida(self):
        self.root.destroy() #Esto destruye todo muajaja :>, osea cierra la ventana
    def ir_entrada(self):
        Entrada(self.root, self.inventario) #El comando instancia la clase hija Entrada, lo hace junto al root y el inventario
    def ir_salida(self):
        Salida(self.root, self.inventario) #El comando instancia la clase hija Salida, lo hace junto al root y el inventario
    def ir_inventario(self):
        Bodega(self.root, self.inventario) #El comando instancia la clase hija Bodega, lo hace junto al root y el inventario
class Entrada(GUI):
    def __init__(self, root, inventario):
        super().__init__(root) #Se hereda el root de la clase padre GUI
        self.inventario = inventario #Refencia el inventario
        self.registrar_entrada() #Y llama al metodo siguiente para crear la pagina de Entrada
    def registrar_entrada(self):
        for widget in self.root.winfo_children(): #Esto es la misma funcion de Volver, por si el usuario estaba en otro apartado y quiere entrar a este, entonces que no se sobreponga
            widget.grid_forget()
        self.create_widgets()
        self.entradaframe = Frame(self.root, bg="#afc7b9", bd=3, relief="ridge") #Se crea el Frame sobre el root, con colorcito, etc.
        self.entradaframe.grid(row=1, column=0, padx=10, pady=10)#Se posiciona en row 1 porque 
        self.entradaframe.config(width="340", height="120")#Se configura el tamaño del frame con pixeles en ancho (width) y alto (height) de 340 y 120, respectivamente
        self.entradaframe.grid_propagate(False) #esto desactiva la propagación de las mismas dimensiones entre un control, widget o grid a la ventana de la aplicación
        #Se crea un texto en plano (Label) sobre el frame con la informacion a decir, color del texto, fondo del texto, tamaño y su posicion en el frame
        Label(self.entradaframe, text="Nombre del Producto:", fg="#20A859", bg="#afc7b9", font=(15)).grid(row=0, column=0)
        #Se crea una caja de texto (Entry) y se posiciona al lado de su Label correspondiente
        self.cuadroNombre = Entry(self.entradaframe)
        self.cuadroNombre.grid(row=0, column=1)
        Label(self.entradaframe, text="Precio del Producto:", fg="#20A859", bg="#afc7b9", font=(15)).grid(row=1, column=0)
        self.cuadroPrecio = Entry(self.entradaframe)
        self.cuadroPrecio.grid(row=1, column=1)
        Label(self.entradaframe, text="Cantidad a ingresar:", fg="#20A859", bg="#afc7b9", font=(15)).grid(row=2, column=0)
        self.cuadroCantidad = Entry(self.entradaframe)
        self.cuadroCantidad.grid(row=2, column=1)
        #Se crea los botones en el frame para Volver, por si te arrepentiste de cada decision de tu vida, y el de enviar_entrada
        Button(self.entradaframe, text="Volver", command=self.volver).grid(row=3, column=0)
        Button(self.entradaframe, text="Enviar", command=self.enviar_entrada).grid(row=3, column=1)
    def enviar_entrada(self): #El metodo de la compra
        nombre = self.cuadroNombre.get() #Se consigue lo que el usuario ingreso en las cajas de texto (.get)
        #Se valida si puso el precio y la cantidad en numeritos, sino da una alerta de error en el messagebox con el except Valueerror y retorna hasta que lo haga bien
        try:
            precio = float(self.cuadroPrecio.get())
            cantidad = int(self.cuadroCantidad.get())
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser números válidos")
            return
        
        tiempo = datetime.datetime.now().strftime('%d-%m-%Y/%H:%M:%S') #Se crea la variable de tiempo con el formato (D/M/A H:M:S)
        producto = Producto(nombre, precio, cantidad, tiempo) #Se instancia lo que se consiguio de las cajas de texto y se crea el objeto de producto
        self.inventario.registrar_entrada(producto, cantidad) #Y se manda al registrar_entrada en el modulo de inventario, el objeto Producto y la cantidad
        messagebox.showinfo("Registro de entrada", f"{producto.nombre} x{cantidad} - {producto.tiempo}") #Y se crea una alerta bonita de que se realizó todo bien
        self.cuadroNombre.delete(0, END) #Al finalizar se borra los datos del Entry para una posible futura compra siguiente
        self.cuadroCantidad.delete(0, END)
        self.cuadroPrecio.delete(0, END)
class Salida(GUI):
    def __init__(self, root, inventario):
        super().__init__(root) #Se hereda el root
        self.inventario= inventario #Referencia el inventario
        self.lista_venta= [] #Se crea una lista para agregar los productos que se van a vender
        self.registrar_salida() #Y se llama al metodo de registrar_salida
    def registrar_salida(self):
        for widget in self.root.winfo_children(): #Se vuelve a hacer el mismo mecanismo de Volver
            widget.grid_forget()
        self.create_widgets()
        self.entradaframe = Frame(self.root, bg="#fca89d", bd=3, relief="ridge") #Se crea el frame en el root que va a contener todo, con su colorcito, etc.
        self.entradaframe.grid(row=1, column=0, padx=10, pady=10) #Se posiciona 
        self.entradaframe.config(width="340", height="120") #Se configura su tamaño
        self.entradaframe.grid_propagate(False) #Se desactiva la propagacion de las dimesiones

        Label(self.entradaframe, text="Nombre del Producto:", fg="#9DF1FC", bg="#fca89d", font=(15)).grid(row=0, column=0) #Se crea los Labels respectivos para la venta
        self.cuadroNombreSalida = Entry(self.entradaframe) #Se crea los Entry
        self.cuadroNombreSalida.grid(row=0, column=1) #Y se posicionan
        Label(self.entradaframe, text="Cantidad a registrar:", fg="#9DF1FC", bg="#fca89d", font=(15)).grid(row=1, column=0)
        self.cuadroCantidadSalida = Entry(self.entradaframe)
        self.cuadroCantidadSalida.grid(row=1, column=1)

        Button(self.entradaframe, text="Volver", command=self.volver).grid(row=2, column=0) #Se crea el boton de Volver
        Button(self.entradaframe, text="Añadir al carrito", command=self.carrito).grid(row=2, column=1) #Se crea boton para añadir el producto a un carrito
        Button(self.entradaframe, text="Ver carrito", command=self.resumen_de_venta).grid(row=3, column=1) #Se crea boton para pasar a la siguiente fase de la venta
    def carrito(self):
        self.inventario.cargar_datos()#Se carga los datos del excel a la lista de inventario
        nombre = self.cuadroNombreSalida.get()#Se consigue lo que se ingreso en los Entry
        try:
            cantidad = int(self.cuadroCantidadSalida.get()) #Si no puso la cantidad en digitos, salta error y retorna
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número válido")
            return
        
        producto_encontrado = False #Se declara que el producto no fue encontrado por si acaso
        for p in self.inventario.productos: #Recorre la lista de inventario
            if p.nombre == nombre and p.cantidad >= cantidad: #Valida si esta y si hay stock
                self.lista_venta.append([nombre, cantidad, p.precio]) #Lo agrega a la lista_venta
                print(self.lista_venta)
                producto_encontrado = True #Ahi si se declara que fue encontrado
                messagebox.showinfo("Agregado", "Se agregó exitosamente al carrito") #Salta una alerta bonita de que se agregó chimba
                self.cuadroNombreSalida.delete(0, END)#Se borra los datos del Entry despues de añadir al carrito, para continuar agregando y promover el capitalismo muajaja
                self.cuadroCantidadSalida.delete(0, END)
                self.inventario.productos.clear()
                break
                
        if not producto_encontrado: #Y si sigue siendo false pues salta un error
            messagebox.showerror("Error", "Producto no encontrado o no hay en bodega")
    def resumen_de_venta(self):
        self.inventario.cargar_datos() #Ya es costumbre esto
        for widget in self.root.winfo_children(): #Y esto
            widget.grid_forget()
        self.create_widgets()

       
        contenedor_frame = Frame(self.root, bg="#fca89d", bd=3, relief="ridge") #Crea un Frame contenedor
        contenedor_frame.grid(row=1, column=0, padx=10, pady=10) #Se posiciona, y se hace que se pegue a todos los lados del root (sticky)
        canvas = Canvas(contenedor_frame, bg="#afc7b9", bd=3) #Se crea un Canvas para permitir poner una scrollbar
        canvas.grid(row=0, column=0, sticky='nsew') #Se posiciona el Canvas
        scrollbar = Scrollbar(contenedor_frame, orient="vertical", command=canvas.yview) #Se agrega una scrollbar vertical al canvas
        scrollbar.grid(row=0, column=1, sticky='ns') #Se posiciona y hace que se pegue arriba y abajo del contenedor
        canvas.configure(yscrollcommand=scrollbar.set) #Y se configura los comandos

        
        ventas_frame = Frame(canvas, bg="#e6ebe8") #Se crea un Frame dentro del Canvas para los items de la venta
        canvas.create_window((0, 0), window=ventas_frame, anchor='nw')

        #Se crea los Labels que muestren la información
        Label(ventas_frame, text="Nombre", fg="#030303", bg="#e6ebe8", font=(15)).grid(row=0, column=0)
        Label(ventas_frame, text="Cantidad", fg="#030303", bg="#e6ebe8", font=(15)).grid(row=0, column=1)
        Label(ventas_frame, text="Precio", fg="#030303", bg="#e6ebe8", font=(15)).grid(row=0, column=2)
        Label(ventas_frame, text="Total", fg="#030303", bg="#e6ebe8", font=(15)).grid(row=0, column=3)
    
        
        total_a_pagar= 0 #Se crea una variable en 0 para el valor total de la venta
        for i,p in enumerate(self.lista_venta): #Se imprimen labels segun cuantos productos son, posicionados con indice por el ennumerate
            Label(ventas_frame, text=f"{p[0]}", fg="#030303", bg="#e6ebe8", font=(15)).grid(row=i+1, column=0, padx=1, pady=1)
            Label(ventas_frame, text=f"x {p[1]}", fg="#030303", bg="#e6ebe8", font=(15)).grid(row=i+1, column=1, padx=1, pady=1)
            Label(ventas_frame, text=f"{p[2]*p[1]}", fg="#030303", bg="#e6ebe8", font=(15)).grid(row=i+1, column=2, padx=1, pady=1)
            total_a_pagar += p[2]*p[1]
        Label(ventas_frame, text=f"{total_a_pagar}", fg="#030303", bg="#e6ebe8", font=(15)).grid(row=1, column=3)

        #Configura el canvas y hace el scrollbar funcional
        ventas_frame.update_idletasks()  # Se asegura de que el tamaño esté calculado antes de usar bbox y la scrollbar abarque todo
        canvas.config(scrollregion=canvas.bbox("all"))

        Button(contenedor_frame, text="Volver", command=self.registrar_salida).grid(row=2, column=0) #Se crea el boton de Volver
        Button(contenedor_frame, text="Pagar", command=lambda: self.elegir_medio_pago(total_a_pagar)).grid(row=3, column=0) #Se crea el boton para seguir con el metodo de pago
    def elegir_medio_pago(self, total_a_pagar):
        # Aquí se permite que el usuario elige entre tarjeta o efectivo
        for widget in self.root.winfo_children():
            widget.grid_forget()
        self.create_widgets()

        self.pago_frame = Frame(self.root, bg="#fca89d", bd=3, relief="ridge") 
        self.pago_frame.grid(row=1, column=0, padx=10, pady=10)
        self.pago_frame.config(width="300", height="75")
        self.pago_frame.grid_propagate(False)

        Label(self.pago_frame, text="Seleccione el método de pago:", fg="#9DF1FC", bg="#fca89d", font=(15)).grid(row=0, column=0, columnspan=2)
        
        Button(self.pago_frame, text="Pagar con Tarjeta", command=lambda: self.pagar_con_tarjeta(total_a_pagar)).grid(row=1, column=0)
        Button(self.pago_frame, text="Pagar en Efectivo", command=lambda: self.pagar_con_efectivo(total_a_pagar)).grid(row=1, column=1)
    def pagar_con_tarjeta(self, total_a_pagar):
        # Se crea una ventana para ingresar los detalles de la tarjeta
        for widget in self.root.winfo_children():
            widget.grid_forget()
        self.create_widgets()

        self.tarjeta_frame = Frame(self.root, bg="#fca89d", bd=3, relief="ridge")
        self.tarjeta_frame.grid(row=1, column=0, padx=10, pady=10)
        self.tarjeta_frame.config(width="450", height="150")
        self.tarjeta_frame.grid_propagate(False)

        Label(self.tarjeta_frame, text="Número de Tarjeta:", fg="#9DF1FC", bg="#fca89d", font=(15)).grid(row=0, column=0)
        self.cuadroNumeroTarjeta = Entry(self.tarjeta_frame) #Se crea un Entry para los valores de la tarjeta
        self.cuadroNumeroTarjeta.grid(row=0, column=1)

        Label(self.tarjeta_frame, text="CVV:", fg="#9DF1FC", bg="#fca89d", font=(15)).grid(row=1, column=0)
        self.cuadroCVV = Entry(self.tarjeta_frame, show="*") #Se crea un Entry para los valores del CVV, por seguridad, cuando se digite los numeros se muestran como *
        self.cuadroCVV.grid(row=1, column=1)

        Button(self.tarjeta_frame, text="Pagar", command=lambda: self.procesar_pago_tarjeta(total_a_pagar)).grid(row=2, column=1)
    def procesar_pago_tarjeta(self, total_a_pagar):
        try:
            numero_tarjeta = self.cuadroNumeroTarjeta.get()#Se consigue los datos del Entry
            cvv = self.cuadroCVV.get()
            if numero_tarjeta.isdigit() and len(numero_tarjeta) == 16: #Se valida si los caracteres del numero_tarjeta sean digitos y si son 16 caracteres, ni mas ni menos
                if cvv.isdigit() and len(cvv) == 3: #Lo mismo con la cvv pero con 3 caracteres
                    self.enviar_salida() #Y ahi se envia a enviar_salida
                    messagebox.showinfo("Pago realizado", f"Pago con tarjeta finalizado: {total_a_pagar}") #Se muestra una alerta bonita de pago realizado
                else:
                    messagebox.showerror("Error", "El CVV debe ser un número de 3 dígitos.") #Muestra un error y enfoca el Entry con problema
                    self.cuadroCVV.focus()#Pone el foco en el campo del CVV 
                    self.cuadroCVV.config(bg="red") #Cambia temporalmente el color de fondo a rojo para resaltar el error
                    self.cuadroCVV.after(1000, lambda: self.cuadroCVV.config(bg="white")) #Luego de un tiempo, vuelve al color normal, con tiempo ajustado a 1 segundo
                    return
            else:
                    #Exactamente el mismo proceso de error que el cvv
                    messagebox.showerror("Error", "El numero de tarjeta debe ser un número de 16 dígitos.")
                    self.cuadroNumeroTarjeta.focus()
                    self.cuadroNumeroTarjeta.config(bg="red")
                    self.cuadroNumeroTarjeta.after(1000, lambda: self.cuadroNumeroTarjeta.config(bg="white"))
                    return
        except Exception as e:
            messagebox.showerror("Error", f"Error en el pago: {str(e)}")
    def pagar_con_efectivo(self, total_a_pagar):
        # Se crea una ventana para ingresar el monto en efectivo
        for widget in self.root.winfo_children():
            widget.grid_forget()
        self.create_widgets()

        self.efectivo_frame = Frame(self.root, bg="#fca89d", bd=3, relief="ridge")
        self.efectivo_frame.grid(row=1, column=0, padx=10, pady=10)
        self.efectivo_frame.config(width="350", height="75")
        self.efectivo_frame.grid_propagate(False)

        Label(self.efectivo_frame, text="Monto entregado:", fg="#9DF1FC", bg="#fca89d", font=(15)).grid(row=0, column=0)
        self.cuadroMontoEfectivo = Entry(self.efectivo_frame)
        self.cuadroMontoEfectivo.grid(row=0, column=1)

        Button(self.efectivo_frame, text="Pagar", command=lambda: self.procesar_pago_efectivo(total_a_pagar)).grid(row=1, column=1)
    def procesar_pago_efectivo(self, total_a_pagar):
        try:
            monto_entregado = float(self.cuadroMontoEfectivo.get()) #Se verifica si el monto entragado es un numero
            if monto_entregado >= total_a_pagar: #Si es mayor o igual al total a pagar
                self.enviar_salida() #Y ahi se envia a enviar_salida
                messagebox.showinfo("Pago realizado", f"Pago en efectivo finalizado: {total_a_pagar} Cambio: {monto_entregado - total_a_pagar}")
            else:
                messagebox.showerror("Pago invalido",f"Fondos insuficientes. Faltan {total_a_pagar - monto_entregado} para completar el pago.")
        except ValueError:
            messagebox.showerror("Error", "Monto entregado no es válido")
    def enviar_salida(self):
        
        self.inventario.productos.clear()
        self.inventario.registrar_salida(self.lista_venta)#Se manda a registrar_salida en el modulo de inventario
        self.lista_venta.clear()#Se limpia la lista_venta
        self.volver()
        self.inventario.productos.clear()
class Bodega(GUI):
    def __init__(self, root, inventario):
        super().__init__(root)
        self.inventario= inventario
        self.mostrar_inventario3()
    def mostrar_inventario(self):
        for widget in self.root.winfo_children():
            widget.grid_forget()
        self.create_widgets()
        self.inventario.cargar_datos()
        inventario_info = ""
        for p in self.inventario.productos:
            inventario_info += f"Nombre {p.nombre}: cantidad: {p.cantidad} x ${p.precio} {p.tiempo}\n"
        if not inventario_info:
            inventario_info = "El inventario está vacío."
        messagebox.showinfo("Inventario", inventario_info)      
    def mostrar_inventario2(self):
        for widget in self.root.winfo_children():
            widget.grid_forget()
        self.create_widgets()
        self.inventario.cargar_datos()
        self.entradaframe = Frame(self.root, bg="#fca89d", bd=3, relief="ridge")
        self.entradaframe.grid(row=1, column=0, padx=10, pady=10)
        self.entradaframe.config(width="450", height="150")
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
        Button(self.entradaframe, text="Volver", command=self.volver).grid(row=0, column=4, padx=10)
        self.inventario.productos.clear()
    def mostrar_inventario3(self):
        os.system("start C:/Users/david/POO/Reto_1/inventario.xlsx")




