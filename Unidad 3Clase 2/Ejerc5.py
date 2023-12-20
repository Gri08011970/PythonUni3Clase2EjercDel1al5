import random
from collections import Counter

#Unidad 3 clase 2 ejercicio 5. Molina Grisleda


def numero_mas_repetido():
    lista_numeros = [random.randint(1, 10) for _ in range(50)]
    contador_numeros = Counter(lista_numeros)
    numero_mas_comun = contador_numeros.most_common(1)[0][0]
    return numero_mas_comun

 
numero_repetido = numero_mas_repetido()
print(f"El número que más se repite es: {numero_repetido}")
