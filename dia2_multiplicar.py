num = int(input('Ingrese un numero')) #ingreso el numero que quiero multiplicar

for c in range(1,11):  # creo un bucle que me itere por la cantidad de numeros que quiero 
    resultado = int(num*c) #creo una variable que me realice la operacion de multiplicacion 
    print (f'{num}x{c}={resultado}') #imprimo y le agrego f para poder ingresar variables dentro del string