
#Unidad 4 ejerccio 7 Molina Griselda

def modificar(lista):
    lista_modificada = list(set(lista))  # Eliminar elementos duplicados
    lista_modificada.sort(reverse=True)  # Ordenar de mayor a menor

    lista_modificada = [num for num in lista_modificada if num % 2 == 0]  # Eliminar números impares

    suma = sum(lista_modificada)  # Sumar los números restantes
    lista_modificada.insert(0, suma)  # Añadir la suma como primer elemento de la lista

    return lista_modificada


numeros = [3, 5, 2, 7, 3, 8, 2, 5]
lista_modificada = modificar(numeros)
print("Lista modificada:", lista_modificada)

# Verificar si el primer elemento coincide con la suma de los demás elementos
suma_resto_elementos = sum(lista_modificada[1:])
if lista_modificada[0] == suma_resto_elementos:
    print("El primer elemento coincide con la suma de los demás elementos.")
else:
    print("El primer elemento NO coincide con la suma de los demás elementos.")
