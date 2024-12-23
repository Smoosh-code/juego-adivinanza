import random

numerosecreto = random.randint(1, 100)
cantidad_intentos = 0
cantidad_maximas = 5
adivinado = False

print("Bienvenido al juego de adivinar el número secreto")

while not adivinado:
    if not cantidad_intentos < cantidad_maximas:
        print("Game Over, no has podido adivinar dentro de los 5 intentos")
        break

    entrada = input("Introduce un número del  1 al 99: ")
    numero = int(entrada)
    if numero == numerosecreto:
        print("¡Felicidades, has adivinado el número secreto!")
        adivinado = True
    elif numero < numerosecreto:
        print("El numero es mayor al ingresado")
    else:
        ("el numero es menor al ingresado")

    cantidad_intentos += 1
