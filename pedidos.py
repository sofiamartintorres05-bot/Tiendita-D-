class Pedido:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def mostrar_pedido(self):
        total = 0
        print("\n--- MI PEDIDO ---")

        for producto, cantidad in self.items:
            valor_unitario = producto.precio
            subtotal = valor_unitario * cantidad
            total += subtotal

            print("Producto:", producto.nombre)
            print("Cantidad:", cantidad)
            print("Valor unitario:", f"${valor_unitario:,.0f}".replace(",", "."))
            print("Subtotal:", f"${subtotal:,.0f}".replace(",", "."))
            print("-----")

        print("TOTAL:", f"${total:,.0f}".replace(",", "."))