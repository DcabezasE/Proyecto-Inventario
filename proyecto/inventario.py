import datetime


class Inventario:
    def __init__(self):
        self.productos = []
        self.fecha_hora= datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    def registrar_entrada(self, producto, cantidad):
        for i in self.productos:
            if i.nombre == producto.nombre:
                i.cantidad += cantidad
                break
        else:
            self.productos.append(producto)
        print(f"Registro de entrada: {producto.nombre} x{cantidad} - {self.fecha_hora}")

    def registrar_salida(self, producto, cantidad):
        for i in self.productos:
            if i.nombre == producto.nombre:
                if i.cantidad >= cantidad:
                    i.cantidad -= cantidad
                    print(f"Registro de salida: {producto.nombre} x{cantidad} - {datetime.date.today()}")
                else:
                    print("No hay suficiente stock")
                break
        else:
            print("Producto no encontrado")

    def obtener_inventario(self):
        print("Inventario actual:")
        for i in self.productos:
            print(f"{i.nombre}: {i.cantidad} x ${i.precio}")


    

