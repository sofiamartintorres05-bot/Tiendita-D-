class Pedido:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def mostrar_pedido(self):
        total = 0
        for producto, cantidad in self.items:
            subtotal = producto.precio * cantidad
            total += subtotal
            print(producto.nombre, cantidad, subtotal)
        print("Total:", total)