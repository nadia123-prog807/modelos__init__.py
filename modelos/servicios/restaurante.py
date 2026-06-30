# Clase que administra los productos

class Restaurante:

    def __init__(self):
        self.productos = []

    # Agregar productos
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Mostrar todos los productos
    def mostrar_productos(self):

        print("\n========== PRODUCTOS DEL RESTAURANTE ==========\n")

        for producto in self.productos:
            producto.mostrar_informacion()
