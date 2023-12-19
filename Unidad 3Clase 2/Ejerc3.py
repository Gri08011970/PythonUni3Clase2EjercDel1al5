#Unidad 3 clase 2 ejercicio 3. Molina Grisleda


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejemplo 
numero = int(input("Ingresa un número entero para verificar si es primo: "))

if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

