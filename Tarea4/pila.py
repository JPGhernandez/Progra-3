print("pila original")
pila=[0,1,2,3,4,5,6,7]
datos=[8,9,10]
print(pila, "\n")
head: int

def push():
    print("pila con elementos agregados")
    

    for n in datos:
        pila.append(n)

    print(pila, "\n")
   

def pop():

    print("elementos eliminados de la pila")
    n= pila.pop()
    print(f"el elemento eliminado es: {n}")
    n= pila.pop()
    print(f"el elemento eliminado es: {n}")
    n= pila.pop()
    print(f"el elemento eliminado es: {n}")
    print("\n")

    print("pila actualizada")
    print(pila)

def peek():
    head = pila.peek()

# push()
# pop()

