class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def setNext(self, nextNode):
        self.next = nextNode

    def setPrev(self, prevNode):
        self.prev = prevNode

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getValue(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.setNext(new_node)
            new_node.setPrev(self.last)
            self.last = new_node

    def insert(self, value, index):
        new_node = Node(value)
        if index == 0:
            new_node.setNext(self.first)
            self.first = new_node
        else:
            current = self.first
            for _ in range(index - 1):
                if current is None:
                    raise IndexError("Index out of bounds")
                current = current.getNext()
            new_node.setNext(current.getNext())
            current.setNext(new_node)

    def remove(self, index):
        if index == 0:
            self.first = self.first.getNext()
        else:
            current = self.first
            for _ in range(index - 1):
                if current is None:
                    raise IndexError("Index out of bounds")
                current = current.getNext()
            if current.getNext() is None:
                raise IndexError("Index out of bounds")
            current.setNext(current.getNext().getNext())

    def swap(self, index1, index2):
        if index1 == index2:
            return
        prev1 = None
        current1 = self.first
        for _ in range(index1):
            if current1 is None:
                raise IndexError("Index out of bounds")
            prev1 = current1
            current1 = current1.getNext()

        prev2 = None
        current2 = self.first
        for _ in range(index2):
            if current2 is None:
                raise IndexError("Index out of bounds")
            prev2 = current2
            current2 = current2.getNext()

        if prev1 is None:
            self.first = current2
        else:
            prev1.setNext(current2)

        if prev2 is None:
            self.first = current1
        else:
            prev2.setNext(current1)

        temp = current1.getNext()
        current1.setNext(current2.getNext())
        current2.setNext(temp)

    def get(self, index):
        current = self.first
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.getNext()
        if current is None:
            raise IndexError("Index out of bounds")
        return current.getValue()


# Membuat objek dari class LinkedList
test_list = LinkedList()

# Menambah beberapa value ke test_list
test_list.add(10)
test_list.add(20)
test_list.add(30)
test_list.add(40)
test_list.add(50)

# Memasukkan sebuah value ke test_list dengan index yang spesifik
test_list.insert(1, 5)

# Display Linked List
print('Semua nilai di test_list:')
for i in range(5):
    print(test_list.get(i))

# Mengubah posisi dua buah value dengan menggunakan indexnya
test_list.swap(1, 5)

# List setelah diubah
print("test_list setelah menggunakan fungsi swap() :")
for i in range(5):
    print(test_list.get(i))

# Menghapus sebuah nilai dengan index yang spesifik
test_list.remove(2)

# List setelah menggunakan fungsi remove
print("test_list setelah menghapus sebuah nilai spesifik menggunakan fungsi remove() :")
for i in range(5):
    print(test_list.get(i))