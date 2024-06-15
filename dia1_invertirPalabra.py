def invertir_caracteres(palabra):
    return palabra [::-1]

palabra_usuario = input("Ingrese una palabra:")

palabra_invertida = invertir_caracteres(palabra_usuario)

print(palabra_invertida)