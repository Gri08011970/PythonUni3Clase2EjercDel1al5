#Unidad 4 ejerccio 6 Molina Griselda

def lista(argumentos):
    if isinstance(argumentos, list):
        print(argumentos)
        print(len(argumentos))
    else:
        print("El argumento no es una lista.")


lista([1, 'hola', ['a', 'b', 'c']])
lista("No soy una lista")
