from productos import listar_productos
from pedidos import Pedido
from historial import guardar_compra, mostrar_historial

pedido_actual = Pedido()

while True:
    print("\n--- MENU ---")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Ver pedido")
    print("4. Historial")
    print("5. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        productos = listar_productos()
        print("\n--- PRODUCTOS ---")
        for i, p in enumerate(productos):
            precio = f"${p.precio:,.0f}".replace(",", ".")
            print(i, p.nombre, precio)

    elif opcion == "2":
        productos = listar_productos()
        print("\n--- PRODUCTOS ---")
        for i, p in enumerate(productos):
            precio = f"${p.precio:,.0f}".replace(",", ".")
            print(i, p.nombre, precio)

        i = int(input("Seleccione producto: "))
        cantidad = int(input("Cantidad: "))
        pedido_actual.agregar_producto(productos[i], cantidad)

    elif opcion == "3":
        pedido_actual.mostrar_pedido()

    elif opcion == "4":
        mostrar_historial()

    elif opcion == "5":
        guardar_compra(pedido_actual)
        print("Compra guardada. Hasta luego.")
        break

    else:
        print("Opción inválida")