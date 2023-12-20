#Unidad 5 ejercicio 2 Molina Griselda
# Crear una lista con los números enteros del 50 al 200
numeros = list(range(50, 201))

# Utilizar map con una función lambda para calcular el cuadrado de cada número
cuadrados = list(map(lambda x: x ** 2, numeros))

print(cuadrados)
