class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def mostrar(self):
        return self.items


def main():
    cola = Cola()

    print("Ingrese elementos a la cola (escriba 'fin' para terminar):")
    while True:
        entrada = input("Elemento: ")

        if entrada.lower() == 'fin':
            break

        try:
            elemento = int(entrada)
        except ValueError:
            elemento = entrada

        cola.encolar(elemento)

    print("\nElementos de la cola:", cola.mostrar())

    if not cola.esta_vacia():
        while True:
            opcion = input("\n¿Qué elemento desea quitar? (escriba 'fin' para terminar): ")

            if opcion.lower() == 'fin':
                break

            try:
                elemento_quitar = int(opcion)
                if elemento_quitar in cola.mostrar():
                    cola.items.remove(elemento_quitar)
                    print(f"Elemento {elemento_quitar} eliminado.")
                    print("Cola actualizada:", cola.mostrar())
                else:
                    print("El elemento no está en la cola.")
            except ValueError:
                print("Por favor, ingrese un número entero.")

    print("\nCola final:", cola.mostrar())


if __name__ == "__main__":
    main()
