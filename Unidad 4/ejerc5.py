#Unidad 4 ejerccio 5 Molina Griselda

def elevar_al_cubo(numero):
    return numero ** 3

while True:
    numero = float(input("Ingresa un número (o ingresa 0 para salir): "))
    
    if numero == 0:
        print("Saliendo del programa...")
        break
    
    resultado = elevar_al_cubo(numero)
    print(f"El resultado de elevar {numero} al cubo es: {resultado}")
