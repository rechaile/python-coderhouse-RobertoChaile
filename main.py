import producto
import cliente


def main():
    # Creación de un cliente
    cliente = cliente.Cliente("Juan", "Pérez", "juan.perez@gmail.com", "123456789")

    # Creación de un producto
    producto = producto.Producto("Televisor 55 pulgadas", "Televisor LED de 55 pulgadas con resolución 4K", 10000)

    # Compra del producto
    cliente.comprar(producto)


if __name__ == "__main__":
    main()