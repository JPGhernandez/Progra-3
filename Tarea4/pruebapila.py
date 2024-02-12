class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "-"
            cur = cur.next
        return out[:-1]
 
    def getSize(self):
        return self.size
 
    def isEmpty(self):
        return self.size == 0
 
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

def reverse_stack(stack):
    temp_stack = Stack()  

    while not stack.isEmpty():
        temp_stack.push(stack.pop())

    return temp_stack
 
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack - push : {stack}")
    print(f"Peek {stack.peek()}")

    # Invertir la pila
    stack = reverse_stack(stack)
    print(f"Stack - reversed: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack - pop: {stack}")
