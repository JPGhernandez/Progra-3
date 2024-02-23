#inicializamos una pila para rastrear los parentesis de apertura
def paréntesis_balanceados(cadena):
    pila = [] 
    parejas = {')': '('} #definimos un diccionario que contiene las parejas de parentesis

    for carácter in cadena: #iteramos sobre cada caracter en la cadena
        if carácter in parejas.values(): #si el caracter es un parentesis de apertuda lo añadimos a la pila
            pila.append(carácter)

        elif carácter in parejas.keys(): # verifica si el caracter es un parentesis de cierre 

             # Verificamos si la pila está vacía o si el paréntesis de apertura correspondiente no está en el tope de la pila
            if not pila or parejas[carácter] != pila.pop():
                return False
        else:     # Si el carácter no es un paréntesis, continuamos con la siguiente iteración
            continue

    return not pila 

# Pedir al usuario que ingrese la cadena de paréntesis
cadena = input("Ingrese la cadena de paréntesis: ")

#Verificar si los paréntesis están balanceados
if paréntesis_balanceados(cadena):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")
