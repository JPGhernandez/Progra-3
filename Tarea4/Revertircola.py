class Cola:
    def __init__(self):
        #inicializa una cola vacia representada por una lista
        self.items = []

#añadimos un elemento al final de la cola
    def enqueue(self, elemento):
        self.items.append(elemento)

#se elimina y devuelve el primer elemento de la cola
    def dequeue(self):

        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            print("La cola está vacía")

#devuelve el primer elemento de la cola sin eliminarlo
    def front(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            print("La cola está vacía")

#analiza si la cola esta vacia 
    def esta_vacia(self):
        return len(self.items) == 0

def revertir_mitad_cola(cola):
    pila = []

    # Calculamos la longitud de la cola
    longitud_cola = len(cola.items)

    # Calculamos el tamaño de la cola dividido 2
    mitad_longitud = longitud_cola // 2

    # Desencolamos y apilamos la primera mitad de los elementos en la pila
    for _ in range(mitad_longitud):
        pila.append(cola.dequeue())

    # Revertimos los elementos en la pila
    while pila:
        cola.enqueue(pila.pop())

    # Volvemos a encolar los elementos de la cola original
    # que no fueron desencolados inicialmente
    for _ in range(longitud_cola - mitad_longitud):
        cola.enqueue(cola.dequeue())

#inicializamos un menu
if __name__ == "__main__":
    # Creamos una cola de ejemplo
    mi_cola = Cola()
    for i in range(1, 11):
        mi_cola.enqueue(i)

    print("Cola original:", mi_cola.items)

    # Aplicamos la función para revertir la mitad de los elementos
    revertir_mitad_cola(mi_cola)

    print("Cola con la mitad revertida:", mi_cola.items)
