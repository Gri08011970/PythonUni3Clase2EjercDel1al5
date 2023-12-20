#Unidad 5 ejercicio 3 Molina Griselda

es_primo = lambda num: all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and num > 1

numeros = list(range(2000, 3001))

# Usar filter con la función lambda para obtener los números primos
numeros_primos = list(filter(es_primo, numeros))

print(numeros_primos)
