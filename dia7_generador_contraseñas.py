# Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.

import random
import string

def generar_contraseña(longitud, excluir_minusculas=False, excluir_mayusculas=False, excluir_digitos=False, excluir_simbolos=False, caracteres_adicionales=""):
    # ... (código similar a la función original)

    # Filtrar caracteres según las opciones del usuario
    caracteres_permitidos = string.ascii_letters
    if not excluir_minusculas:
        caracteres_permitidos += string.ascii_lowercase
    if not excluir_mayusculas:
        caracteres_permitidos += string.ascii_uppercase
    if not excluir_digitos:
        caracteres_permitidos += string.digits
    if not excluir_simbolos:
        caracteres_permitidos += string.punctuation
    if caracteres_adicionales:
        caracteres_permitidos += caracteres_adicionales

    # ... (resto del código de generación de contraseña)

# Ejemplo de uso con opciones
contrasena1 = generar_contraseña(12, excluir_simbolos=True, caracteres_adicionales="@#$")
contrasena2 = generar_contraseña(15, excluir_minusculas=True)

print(f"Contraseña 1 (sin símbolos, con @#$): {contrasena1}")
print(f"Contraseña 2 (sin minúsculas): {contrasena2}")

