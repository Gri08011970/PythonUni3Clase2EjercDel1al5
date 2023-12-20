#Unidad 4 ejerccio 3 Molina Griselda

def modulo_1():
    print("Bienvenido al Módulo 1")
    print("Aquí puedes realizar ciertas operaciones...")
    # Funcionalidad del módulo 1

def modulo_2():
    print("Bienvenido al Módulo 2")
    print("Este módulo ofrece diferentes herramientas...")
    # Funcionalidad del módulo 2

def modulo_3():
    print("Bienvenido al Módulo 3")
    print("En este módulo puedes acceder a otras opciones...")
    # Funcionalidad del módulo 3

def modulo_4():
    print("Bienvenido al Módulo 4")
    print("Aquí encontrarás diferentes funcionalidades...")
    # Funcionalidad del módulo 4

while True:
    print("\nMenú:")
    print("1. Módulo 1")
    print("2. Módulo 2")
    print("3. Módulo 3")
    print("4. Módulo 4")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == '1':
        modulo_1()
    elif opcion == '2':
        modulo_2()
    elif opcion == '3':
        modulo_3()
    elif opcion == '4':
        modulo_4()
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Ingresa un número del 1 al 5.")
