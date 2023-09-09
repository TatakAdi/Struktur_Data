class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self, next_node):
        self.next = next_node


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.setNext(self.top)
            self.top = new_node

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        popped_value = self.top.getValue()
        self.top = self.top.getNext()
        return popped_value

    def hasPop(self):
        return not self.isEmpty()

    def swap(self):
        if self.top is None or self.top.getNext() is None:
            return
        first_node = self.top
        second_node = self.top.getNext()
        first_value = first_node.getValue()
        second_value = second_node.getValue()
        first_node.value = second_value
        second_node.value = first_value

    def display(self):
        current = self.top
        while current is not None:
            print(current.getValue(), end=", ")
            current = current.getNext()
        print()


# Contoh penggunaan
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Before swap:")
print("Top:", stack.top.getValue())  # Output: 30
print("Second:", stack.top.getNext().getValue())  # Output: 20

stack.swap()

print("\nAfter swap:")
print("Top:", stack.top.getValue())  # Output: 20
print("Second:", stack.top.getNext().getValue())  # Output: 30
stack.display()
stack.pop()
stack.display()
