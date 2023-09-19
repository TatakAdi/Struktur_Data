def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
bubble_sort(arr1)
print(arr1)
