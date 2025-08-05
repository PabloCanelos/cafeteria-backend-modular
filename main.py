def mostrar_menu():
    print("==  MENU PRINCIPAL  ==")
    print("Si desea salir de alguna opción escriba 'salir'")
    print("1) Registrar pedidos")
    print("2) Consultar disponibilidad de productos")
    print("3) Validar entradas de usuario")
    print("4) Consultar estadísticas")
    print("5) Salir")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Llamar a order.py para registrar pedido
            pass
        elif opcion == "2":
            # Llamar a menu.py para ver productos
            pass
        elif opcion == "3":
            # Usar validate.py para validar entrada
            pass
        elif opcion == "4":
            # Mostrar estadísticas desde order.py
            pass
        elif opcion == "5" or opcion.lower() == "salir":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar()