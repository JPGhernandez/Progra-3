class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def ha_aprobado(self):
        if self.calificacion >= 60:
            return True
        else:
            return False


nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
calificacion = float(input("Ingrese la calificación del estudiante: "))


estudiante = Estudiante(nombre, edad, calificacion)

if estudiante.ha_aprobado():
    print(f"{estudiante.nombre} ha aprobado.")
else:
    print(f"{estudiante.nombre} no ha aprobado.")



