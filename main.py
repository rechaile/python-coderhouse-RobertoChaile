from Modulos import producto as product
from Modulos import cliente



# Creación de un cliente
cliente = cliente.Cliente("Juan", "Pérez", "juan.perez@gmail.com", "123456789")

# Creación de un producto
producto = product.Producto("Televisor 55 pulgadas", "Televisor LED de 55 pulgadas con resolución 4K", 10000)
producto2 = product.Producto("iPhone 15", "Celular iPhone 15 128Gb Camara 8Mpx", 1000)
producto3 = product.Producto("Lavarropas Whirlpool", "Lavarropas de 30lts con velocidad de centrifugado de 1000rpm", 55000)
# Compra del producto
cliente.comprar(producto)
cliente.comprar(producto2)
cliente.agregar_a_favoritos(producto3)

cliente.mostrar_lista_de_compras()
cliente.mostrar_lista_de_favoritos()
cliente.calcular_total()
cliente.mostrar_total()