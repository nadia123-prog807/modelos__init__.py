from modelos.producto import Producto

# Clase hija Bebida

class Bebida(Producto):

    def __init__(self, nombre, precio, disponible, volumen):
        super().__init__(nombre, precio, disponible)
        self.volumen = volumen

    # Polimorfismo
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print("----- BEBIDA -----")
        print("Nombre:", self.nombre)
        print("Precio: $", self.obtener_precio())
        print("Volumen:", self.volumen, "ml")
        print("Estado:", estado)
        print()
