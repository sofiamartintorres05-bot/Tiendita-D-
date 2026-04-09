class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


def listar_productos():
    return [
        Producto("Laptop", 2000000),
        Producto("Mouse", 50000),
        Producto("Teclado", 100000),
        Producto("Monitor", 800000),
        Producto("Audifonos", 150000),
        Producto("Impresora", 600000),
        Producto("USB", 30000)
    ]