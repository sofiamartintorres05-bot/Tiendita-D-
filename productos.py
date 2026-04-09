class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

def listar_productos():
    productos = [
        Producto("Laptop", 2000),
        Producto("Mouse", 50),
        Producto("Teclado", 100)
    ]
    return productos