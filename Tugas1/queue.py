class Que:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


queue = Que()

initial_elements = [1, 2, 3, 4, 5]
for element in initial_elements:
    queue.enqueue(element)

print("Angka sekarang: ", queue.items)

# Tambahkan angka baru
queue.enqueue(6)
queue.enqueue(7)
print("Angka setelah ditambahkan: ", queue.items)

# Keluar angka dari depan
# Jadi tambahkan sebelah kanan keluarkan sebelah kiri
out = queue.dequeue()
print("Angka dihilangkan dari depan: ", out)
print("Angka sekarang: ", queue.items)

out = queue.dequeue()
print("Angka dihilangkan dari depan: ", out)
print("Angka sekarang: ", queue.items)
