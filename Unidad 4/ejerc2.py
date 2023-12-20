# unidad 4 ejercicio 2 Molina Griselda
import random

numeros = [random.randint(1, 20) for _ in range(10)]


print("Lista inicial:")
print(numeros)


numeros_reemplazados = ['PAR' if num % 2 == 0 else num for num in numeros]

print("\nLista con números pares reemplazados por 'PAR':")
print(numeros_reemplazados)
