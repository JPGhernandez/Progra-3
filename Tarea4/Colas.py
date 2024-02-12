#inicializamos una nueva cola vacia
class Cola:
    def __init__(self):
        self.items = []


# Este metodo permite agregar un elemento a la cola
    def enqueue(self, elemento):
        self.items.append(elemento)

# Esta funcion saca elementos de la cola
    def dequeue(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            print("La cola está vacía")

# Esta funcion permite ver el primer elemento de la cola
    def front(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            print("La cola está vacía")
# definir si la cola esta vacia
    def esta_vacia(self):
        return len(self.items) == 0

# Menu de opciones
def simulacion_fila():
    fila = Cola()
    while True:
        print("\nOpciones:")
        print("1. Agregar persona a la fila")
        print("2. Atender persona")
        print("3. Ver primera persona en la fila")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la persona: ")
            fila.enqueue(nombre)
            print(f"{nombre} ha sido agregado a la fila.")

        elif opcion == "2":
            if not fila.esta_vacia():
                persona_atendida = fila.dequeue()
                print(f"{persona_atendida} ha sido atendida.")
            else:
                print("La fila está vacía.")

        elif opcion == "3":
            if not fila.esta_vacia():
                print(f"La primera persona en la fila es: {fila.front()}")
            else:
                print("La fila está vacía.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    simulacion_fila()
