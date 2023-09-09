class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack masih kosong")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def swap(self):
        if len(self.items) > 2:
            self.items[-1], self.items[-2] = self.items[-2], self.items[-1]
        else:
            return stack


stack = Stack()
# pop saat stack masih kosong
stack.pop()

initial_elements = [1, 2, 3, 4, 5]
for element in initial_elements:
    stack.push(element)

print("Angka sekarang:", stack.items)

# Menambahkan angka baru
# stack.push(6)
# stack.push(7)
print("Angka setelah ditambah di belakang:", stack.items)

# Menghapus angka dari belakang
# Menambahkan angka sebelah kanan dan keluarkan angka sebelah kanan juga
out = stack.pop()
print("Angka dihilangkan dari bagian belakang:", out)
print("Angka hasilnya:", stack.items)

# Menukar posisi dua angka yang berada di sebelah kanan stack
stack.swap()
print("Stack setelah ditukar posisinya : ", stack.items)
