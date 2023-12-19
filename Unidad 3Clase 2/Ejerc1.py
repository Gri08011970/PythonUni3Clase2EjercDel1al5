#Unidad 3 clase 2 ejercicio 1. Molina Grisleda


def obtener_vocales(frase):
    vocales = [letra for letra in frase if letra.lower() in 'aeiouáéíóúü']
    return ''.join(vocales)

def obtener_consonantes(frase):
    consonantes = [letra for letra in frase if letra.lower() not in 'aeiouáéíóúü' and letra.isalpha()]
    return ''.join(consonantes)

def main():
    frase = input("Ingresa una frase: ")

    print("\nFrase original:", frase)
    print("Vocales:", obtener_vocales(frase))
    print("Consonantes:", obtener_consonantes(frase))

if __name__ == "__main__":
    main()
