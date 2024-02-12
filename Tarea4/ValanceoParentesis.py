def paréntesis_balanceados(cadena):
    pila = []
    parejas = {')': '('}

    for carácter in cadena:
        if carácter in parejas.values():
            pila.append(carácter)
        elif carácter in parejas.keys():
            if not pila or parejas[carácter] != pila.pop():
                return False
        else:
            continue

    return not pila

# Pedir al usuario que ingrese la cadena de paréntesis
cadena = input("Ingrese la cadena de paréntesis: ")

# Verificar si los paréntesis están balanceados
if paréntesis_balanceados(cadena):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")
