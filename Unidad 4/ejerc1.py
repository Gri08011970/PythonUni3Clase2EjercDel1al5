#Unidad 4 ejerccio 1 Molina Griselda

def ingresar_palabras():
    palabras = []
    for _ in range(10):
        palabra = input("Ingresa una palabra: ")
        palabras.append(palabra)
    return palabras

def verificar_existencia_palabra(palabras):
    palabra_buscada = input("Ingresa una palabra para verificar si está en la lista anterior: ")
    if palabra_buscada in palabras:
        print(f"La palabra '{palabra_buscada}' está en la lista de palabras ingresadas anteriormente.")
    else:
        print(f"La palabra '{palabra_buscada}' no está en la lista de palabras ingresadas anteriormente.")


print("Ingresa 10 palabras:")


lista_palabras = ingresar_palabras()
print("\nAhora ingresa una palabra para verificar si está en la lista anterior:")
verificar_existencia_palabra(lista_palabras)
