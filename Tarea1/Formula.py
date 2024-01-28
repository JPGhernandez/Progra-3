import cmath  

def formula(a, b, c):
   
    discriminante = cmath.sqrt(b**2 - 4*a*c)

    
    solucion1 = (-b + discriminante) / (2*a)
    solucion2 = (-b - discriminante) / (2*a)

    return solucion1, solucion2


a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

solucion1, solucion2 = formula(a, b, c)


print(f"Las soluciones son: {solucion1} y {solucion2}")
