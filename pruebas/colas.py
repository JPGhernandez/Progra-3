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

    print("\nElementos de la cola:")
    while not cola.esta_vacia():
        print(cola.desencolar())


if __name__ == "__main__":
    main()
