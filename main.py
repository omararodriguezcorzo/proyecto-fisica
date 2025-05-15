from menu_y_entradas.menu import mostrar_menu
from conversiones.longitud.metro import recolectar_unidades, mostrar_conversiones
from conversiones.notaciones.notaciones import decimal_a_cientifica, cientifica_a_decimal
from conversiones.vectores.metodo_del_triangulo.triangulo import obtener_componentes, calcular_resultante

def conversion_metros():
    try:
        metros = float(input("Introduce el valor en metros: "))
        datos = recolectar_unidades(metros)
        mostrar_conversiones(datos, metros)
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")

def conversion_notaciones():
    opcion = input("a) Decimal a científica\nb) Científica a decimal\nSelecciona una opción (a/b): ").strip().lower()

    if opcion == "a":
        try:
            numero = float(input("Introduce un número decimal: "))
            print("Notación científica:", decimal_a_cientifica(numero))
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar un número.")

    elif opcion == "b":
        notacion = input("Introduce la notación científica (ej: 1.23e4): ")
        try:
            decimal = cientifica_a_decimal(notacion)
            print("Número decimal:", decimal)
        except ValueError:
            print("Formato inválido. Usa una forma como '1.2e3'")
    else:
        print("Opción no válida.")


def suma_vectores():
    try:
        num_vectores = int(input("¿Cuántos vectores quieres sumar? "))
        vectores = []

        for i in range(num_vectores):
            print(f"\nVector {i + 1}:")
            magnitud = float(input("  Magnitud: "))
            direccion = input("  Dirección (N, S, E, O, NE, NO, SE, SO): ")
            componentes = obtener_componentes(magnitud, direccion)
            vectores.append(componentes)

        R_x, R_y, magnitud_R, angulo_R = calcular_resultante(vectores)

        print("\n=== RESULTADO ===")
        print(f"Vector resultante: ({R_x:.2f}, {R_y:.2f})")
        print(f"Magnitud: {magnitud_R:.2f}")
        print(f"Ángulo: {angulo_R:.2f}°")
    except ValueError:
        print("Entrada inválida.")

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            conversion_metros()
        elif opcion == "2":
            conversion_notaciones()
        elif opcion == "3":
            suma_vectores()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
