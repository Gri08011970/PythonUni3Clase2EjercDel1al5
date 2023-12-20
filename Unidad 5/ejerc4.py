#Unidad 5 ejercicio 4 Molina Griselda
from functools import reduce


numeros = list(range(1, 101))

# Utilizar reduce con una función lambda para obtener la sumatoria de los elementos de la lista
sumatoria = reduce(lambda x, y: x + y, numeros)

print(sumatoria)
