historial = []

def guardar_compra(pedido):
    historial.append(pedido.items)

def mostrar_historial():
    print("\n--- HISTORIAL DE COMPRAS ---")
    for compra in historial:
        total_compra = 0
        print("\nCompra:")

        for producto, cantidad in compra:
            valor_unitario = producto.precio
            subtotal = valor_unitario * cantidad
            total_compra += subtotal

            print("Producto:", producto.nombre)
            print("Cantidad:", cantidad)
            print("Valor unitario:", f"${valor_unitario:,.0f}".replace(",", "."))
            print("Subtotal:", f"${subtotal:,.0f}".replace(",", "."))
            print("-----")

        print("TOTAL COMPRA:", f"${total_compra:,.0f}".replace(",", "."))