class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None


def main():
    pila = Pila()

    print("Ingrese elementos a la pila (escriba 'fin' para terminar):")
    while True:
        entrada = input("Elemento: ")

        if entrada.lower() == 'fin':
            break

        try:
            elemento = int(entrada)
        except ValueError:
            elemento = entrada

        pila.apilar(elemento)

    print("\nElementos de la pila:")
    while not pila.esta_vacia():
        print(pila.desapilar())


if __name__ == "__main__":
    main()
