#inicializa un nodo con un valor dado y su siguiente nodo con None
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
 #inicializa una pila con un nodo de encabezado y de tamaño 0
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

#en esta funcion retorna una representacion de la pila como una cadena
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "-"
            cur = cur.next
        return out[:-1]
 
 #verificamos el tamaño actual de la pila
    def getSize(self):
        return self.size
 
 #verifica si la pila esta vacia
    def isEmpty(self):
        return self.size == 0
 
 #retorna el valor del elemento superior de la pila sin desapilar los elementos
    def peek(self):
        if self.isEmpty():
            raise Exception("intentando ver el elemento superior de la pila")
        return self.head.next.value
 
 #agregamos un nuevo elemento a la pila 
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
 #eliminamos elementos de la pila
    def pop(self):
        if self.isEmpty():
            raise Exception("desapilando elemento de la pila")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

#funcion para invertir la pila
def reverse_stack(stack):
    temp_stack = Stack()  

    while not stack.isEmpty():
        temp_stack.push(stack.pop())

    return temp_stack
 
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"pila : {stack}")
    print(f"elemento que encabeza la pila {stack.peek()}")

    # Invertimos la pila
    stack = reverse_stack(stack)
    print(f"pila invertida: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"desapilando: {remove}")
    print(f"elementos que quedan en la pila: {stack}")
