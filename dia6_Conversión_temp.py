# Conversión de temperatura:
# Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

# Pedir al usuario que ingrese la temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Aplicar la fórmula de conversión directamente
fahrenheit = celsius * 9/5 + 32

# Imprimir el resultado
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")


# Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.
import random

def obtener_eleccion_computadora():
    return random.choice(["piedra", "papel", "tijeras"])

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijeras") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijeras" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    usuario = input("Elige piedra, papel o tijeras: ").lower()
    computadora = obtener_eleccion_computadora()
    print(f"La computadora eligió: {computadora}")
    resultado = determinar_ganador(usuario, computadora)
    print(f"Resultado: {resultado}")

jugar()
