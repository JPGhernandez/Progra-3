var1=float(input("Digite el primer Numero a Operar: "))
var2=float(input("Digite el segundo numero a operar: "))

suma=var1+var2
resta=var1-var2
mult=var1*var2

if var2!=0:
    div=var1/var2
else:
    div="ingrese un valor diferente de 0"


print(f"Suma: {var1} + {var2} = {suma}")
print(f"Resta: {var1} - {var2} = {resta}")
print(f"Multiplicación: {var1} * {var2} = {mult}")
print(f"División: {var1} / {var2} = {div}")



