import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Membuat fungsi untuk memasukkan angka ke dalam linked list
    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Membuat fungsi untuk menampilkan isi dari linked list
    def tampilkan(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Membuat fungsi untuk mensortir linked list dengan metode bubble sort
    def bubble_sort(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                    print(
                        "Value yang ditukar = {sebelum} dengan {sesudah}".format(
                            sebelum=current.data, sesudah=current.next.data
                        )
                    )
                    self.tampilkan()
                    print(
                        "=============================================================================================================="
                    )
                current = current.next


# Membuat linked list
linked_list = LinkedList()

# Meminta angka dari komputer
for angka in range(101):
    angka_random = random.randint(1, 1000)
    linked_list.push(angka_random)

# Menampilkan isi linke list sebelum dilakukan bubble sorting
print("Linked list sebelum dilakukan bubble sorting")
linked_list.tampilkan()

# Melakukan bubble sorting
print("Linked list saat dilakukan bubble sorting")
linked_list.bubble_sort()

# Menampilkan isi linked list setelah dilakukan bubble sorting
print("Linked list setelah dilakukan bubble sorting")
linked_list.tampilkan()
