def suma_par(var1, var2):
    
    suma = var1 + var2
    
   
    print("La suma de", var1, "y", var2, "es:", suma)

    
    if suma % 2 == 0:
        return True
    else:
        return False


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))


resultado = suma_par(numero1, numero2)
print("¿el resultado de la suma es par?: ", resultado)


    




