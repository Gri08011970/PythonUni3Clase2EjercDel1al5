#Unidad 3 clase 2 ejercicio 2 Molina Griselda

def factorial(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

# Ejemplo 
numero = int(input("Ingresa un número entero positivo para calcular su factorial: "))
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")
