
# Definición de la clase Cliente
class Cliente:

    # Constructor de la clase
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

        # Lista de productos comprados
        self.lista_de_compras = []

        # Lista de productos favoritos
        self.lista_de_favoritos = []

    # Método para comprar un producto
    def comprar(self, producto):

        # Compra el producto
        self.lista_de_compras.append(producto)

        # Devuelve la información del producto
        return f"El cliente {self.nombre} ha comprado el producto {producto.nombre}."

    # Método para agregar un producto a favoritos
    def agregar_a_favoritos(self, producto):
        self.lista_de_favoritos.append(producto)
        print(f"El cliente {self.nombre} ha agregado el producto {producto.nombre} a sus favoritos")

    # Método para mostrar la lista de compras
    def mostrar_lista_de_compras(self):
        print(f"La lista de compras del cliente {self.nombre} es:")
        for producto in self.lista_de_compras:
            print(f"* {producto.nombre}")

    # Método para mostrar la lista de favoritos
    def mostrar_lista_de_favoritos(self):
        print(f"La lista de favoritos del cliente {self.nombre} es:")
        for producto in self.lista_de_favoritos:
            print(f"* {producto.nombre}")
            
    # Método para calcular el total a pagar
    def calcular_total(self):
        total = 0
        for producto in self.lista_de_compras:
            total += producto.precio
        return total
    
    # Método para mostrar el total a pagar
    def mostrar_total(self):
        total = self.calcular_total()
        print(f"El total a pagar es: ${total}")
        
    #Metodo para mostrar nombre de cliente
    
    def __str__(self):
        return f"Cliente {self.nombre} {self.apellido}"