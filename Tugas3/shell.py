import random

def shellSort(array):
    n = len(array)
    step = 1
    while step < n // 2:
        step = step * 3 + 1 

    while step >= 1:
        for i in range(step, n):
            temp = array[i]
            j = i
            while j >= step and array[j - step] > temp:
                array[j] = array[j - step]
                j -= step
            array[j] = temp
        step //= 2


data = [random.randint(1,101) for i in range (100)]
size = len(data)
print('Sebelum sorting:')
print(data)
shellSort(data)
print('Setelah sorting:')
print(data)
