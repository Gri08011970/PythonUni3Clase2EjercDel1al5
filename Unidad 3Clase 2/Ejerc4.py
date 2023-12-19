#Unidad 3 clase 2 ejercicio 4. Molina Grisleda

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_entre_rangos(inicio, fin):
    primos = []
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

# Ejemplo 
inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el fin del rango: "))

resultado = numeros_primos_entre_rangos(inicio, fin)
print(f"Los números primos entre {inicio} y {fin} son: {resultado}")
