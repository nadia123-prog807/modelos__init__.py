# Clase padre Producto

class Producto:

    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.__precio = precio     # Encapsulación
        self.disponible = disponible

    # Método para obtener el precio
    def obtener_precio(self):
        return self.__precio

    # Método para modificar el precio
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio debe ser mayor que cero.")

    # Método que será sobrescrito
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print("Nombre:", self.nombre)
        print("Precio: $", self.__precio)
        print("Estado:", estado)
