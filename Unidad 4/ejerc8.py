
#Unidad 4 ejerccio 8 Molina Griselda
import random
from collections import Counter

# Generar 20 números aleatorios entre 1 y 5 y guardarlos en una lista
numeros = [random.randint(1, 5) for _ in range(20)]

# Mostrar la lista de números generados
print("Lista de números generados:")
print(numeros)

# Contar la frecuencia de cada número
frecuencia_numeros = Counter(numeros)

# Encontrar la frecuencia máxima
frecuencia_maxima = max(frecuencia_numeros.values())

# Encontrar todos los números con la frecuencia máxima
numeros_mas_repetidos = [numero for numero, frecuencia in frecuencia_numeros.items() if frecuencia == frecuencia_maxima]

# Mostrar los números más repetidos
print("\nLos números más repetidos son:")
for numero in numeros_mas_repetidos:
    print(numero)
