# Primero, pedimos al usuario que nos dé una lista de números, separados por comas
numeros_input = input("Introduce una lista de números separados por comas: ")

# Convierto la cadena de entrada en una lista de números
numeros = [int(num) for num in numeros_input.split(",")]

# Ordeno la lista de números en orden ascendente
numeros_ordenados = sorted(numeros)

# Mostramos la lista ordenada al usuario
print("La lista de números ordenada es:", numeros_ordenados)