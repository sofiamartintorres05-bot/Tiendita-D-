historial_archivo = "historial.txt"


def guardar_compra(pedido):
    with open(historial_archivo, "a") as archivo:
        archivo.write("\n--- NUEVA COMPRA ---\n")
        total_compra = 0

        for producto, cantidad in pedido.items:
            valor_unitario = producto.precio
            subtotal = valor_unitario * cantidad
            total_compra += subtotal

            archivo.write(f"Producto: {producto.nombre}\n")
            archivo.write(f"Cantidad: {cantidad}\n")
            archivo.write(f"Valor unitario: ${valor_unitario:,.0f}".replace(",", ".") + "\n")
            archivo.write(f"Subtotal: ${subtotal:,.0f}".replace(",", ".") + "\n")
            archivo.write("-----\n")

        archivo.write(f"TOTAL COMPRA: ${total_compra:,.0f}".replace(",", ".") + "\n")


def mostrar_historial():
    try:
        with open(historial_archivo, "r") as archivo:
            print("\n--- HISTORIAL DE COMPRAS ---")
            print(archivo.read())
    except FileNotFoundError:
        print("No hay historial aún.")