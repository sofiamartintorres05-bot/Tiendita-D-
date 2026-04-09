historial = []

def guardar_compra(pedido):
    historial.append(pedido.items)

def mostrar_historial():
    for compra in historial:
        print("Compra:")
        for producto, cantidad in compra:
            print(producto.nombre, cantidad)