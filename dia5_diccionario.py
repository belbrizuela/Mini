# Escribe un programa que crea un diccionario a partir de dos listas dadas: una de claves y otra de valores.

def crear_diccionario(claves, valores):
    if len(claves) != len(valores): # Verificar que las listas tengan la misma longitud
        raise ValueError("Las listas de claves y valores deben tener la misma longitud")
    
    diccionario = {} # definimos un diccionario vacío

    for i in range(len(claves)): # recorremos ambas listas al mismo tiempo
        
        diccionario[claves[i]] = valores[i] # Asigno cada clave a su correspondiente valor en el diccionario
    
    return diccionario 

# defino la lista
claves = ['a', 'b', 'c']
valores = [1, 2, 3]

# Creo el diccionario
diccionario = crear_diccionario(claves, valores)

# Imprimo el diccionario resultante
print(diccionario)
