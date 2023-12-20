#Unidad 4 ejerccio 4 Molina Griselda

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "No se puede dividir por cero."

while True:
    print("\nMenú:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == '5':
        print("Saliendo del programa...")
        break

    try:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))

        if opcion == '1':
            resultado = suma(num1, num2)
        elif opcion == '2':
            resultado = resta(num1, num2)
        elif opcion == '3':
            resultado = multiplicacion(num1, num2)
        elif opcion == '4':
            resultado = division(num1, num2)
        else:
            print("Opción inválida. Ingresa un número del 1 al 5.")
            continue

        print(f"El resultado de la operación es: {resultado}")

    except ValueError:
        print("Ingresa números enteros válidos.")
    except Exception as e:
        print("Ha ocurrido un error:", e)
