def suma_par(var1, var2, var3, var4):
    
    suma = var1 + var2 + var3 + var4
    
   
    print(f"La suma de", var1, var2, var3, var4," es:", suma)

    
    if suma % 2 == 0:
        return True
    else:
        return False


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el segundo número: "))
numero4 = int(input("Ingrese el segundo número: "))


resultado = suma_par(numero1, numero2,numero3, numero4)
print("¿el resultado de la suma es par?: ", resultado)


    
