def contar_vocales(cadena):
    # Esta es la lista de vocales, tanto en minúsculas como en mayúsculas
    vocales = "aeiouAEIOU"
    contador = 0 # Empezamos con el contador en cero

    for char in cadena: # creo un bucle para revisar cada letra en la cadena que nos dieron
        if char in vocales: # Si la letra es una vocal, aumentamos el contador
            contador += 1
    return contador #Al final, devolvemos el total de vocales que encontramos

# Pedimos al usuario que nos dé una cadena de texto
cadena = input("Introduce una cadena de texto: ")

# Llamo a la función para contar las vocales y guardamos el resultado
numero_vocales = contar_vocales(cadena)

# Mostramos cuántas vocales encontramos
print(f"El número de vocales en la cadena es: {numero_vocales}")
