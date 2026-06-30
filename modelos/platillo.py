from modelos.producto import Producto

# Clase hija Platillo

class Platillo(Producto):

    def __init__(self, nombre, precio, disponible, tipo_platillo):
        super().__init__(nombre, precio, disponible)
        self.tipo_platillo = tipo_platillo

    # Polimorfismo
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print("----- PLATILLO -----")
        print("Nombre:", self.nombre)
        print("Precio: $", self.obtener_precio())
        print("Tipo:", self.tipo_platillo)
        print("Estado:", estado)
        print()
