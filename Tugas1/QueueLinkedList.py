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


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.setNext(new_node)
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        front_value = self.front.getValue()
        self.front = self.front.getNext()
        if self.front is None:
            self.rear = None
        return front_value

    def swap(self):
        if self.front is None or self.front.getNext() is None:
            return
        first_node = self.front
        second_node = self.front.getNext()
        first_value = first_node.getValue()
        second_value = second_node.getValue()
        first_node.value = second_value
        second_node.value = first_value

    def display(self):
        current = self.front
        while current is not None:
            print(current.getValue(), end=" ")
            current = current.getNext()
        print()


# Contoh penggunaan
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue contents:")
queue.display()  # Output: 10 20 30

queue.swap()

print("\nAfter swap:")
queue.display()  # Output: 20 10 30
print("Element yg dihapus : ", queue.dequeue())
print("Isi queue sekarang : ", queue.display())
