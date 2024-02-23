#inicializamos una pila para rastrear los parentesis de apertura
def paréntesis_balanceados(cadena):
    pila = [] #aqui se almacenaran los parentesis que el ususario ingrese
    parejas = {')': '('} #definimos un diccionario que contiene las parejas de parentesis, tiene una key y un value

    for carácter in cadena: 
        if carácter in parejas.values(): #si el caracter es un parentesis de apertuda lo añadimos a la pila
            pila.append(carácter)

        elif carácter in parejas.keys(): # verifica si el caracter es un parentesis de cierre 

            
            #Verifica si la pila está vacía. Si la pila está vacía, significa que no hay ningún paréntesis de apertura que pueda emparejar el paréntesis de cierre actual
         if not pila or parejas[carácter] != pila.pop(): 
                return False
        else:    
            continue

    return not pila 

# Pedir al usuario que ingrese la cadena de paréntesis
cadena = input("Ingrese la cadena de paréntesis: ")

#Verificar si los paréntesis están balanceados
if paréntesis_balanceados(cadena):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")
