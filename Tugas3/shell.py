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

data = [1543, 2341, 7890, 5678, 4321, 9087, 3210, 8765, 4567, 1098, 5432, 9876, 8765, 2310, 5678, 9087, 8765, 1098, 6543, 3210]
print('Sebelum sorting:', data)
shellSort(data)
print('Setelah sorting:', data)
