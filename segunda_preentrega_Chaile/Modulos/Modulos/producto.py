class Producto:

    # Constructor de la clase
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
    
    # Método para mostrar el producto
    def __str__(self):
        return f"Producto {self.nombre} - ${self.precio}"