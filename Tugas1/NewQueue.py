class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("queue masih kosong")

    def swap_last(self):
        if 2 < len(self.items):
            self.items[-1], self.items[-2] = (
                self.items[-2],
                self.items[-1],
            )

    def swap_first(self):
        if 2 < len(self.items):
            self.items[0], self.items[1] = (
                self.items[1],
                self.items[0],
            )

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


queue = Queue()
print("Queue: ", queue.items)
# Melakukan fungsi pop saat queue masih kosong
queue.pop()

# Angka = [10, 20, 30, 40]
# # Melakukan push beberapa angka ke dalam queue
# for que in Angka:
#     queue.push(que)

print("queue: ", queue.items)
# Melakukan push beberapa huruf ke dalam queue
queue.push("a")
queue.push("b")
queue.push("c")
queue.push("d")
queue.push("e")

print("Queue:", queue.items)
# Melakukan pop beberapa element yang berada di dalam queue
i = 0
while i < queue.size():
    popped_item = queue.pop()
    print("Item yang di-pop:", popped_item)
    print("Queue setelah pop:", queue.items)
    i += 1

# Melakukan swap pada beberapa element queue yang berada di ujung kanan dan kiri queue
queue.swap_last()
queue.swap_first()
print("Queue setelah swap:", queue.items)
