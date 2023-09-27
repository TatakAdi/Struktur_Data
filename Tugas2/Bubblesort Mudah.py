def bubble_sort(array):
    n = len(array)
    langkah = 1
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                print ("langkah {} = {}".format(langkah,array))
                langkah += 1


arr1 = [95,88,92,84,97,89,91,99,86,93,87,96,83,90,100,94,82,98,85,81]
print("Sebelum disortir : ", arr1)
bubble_sort(arr1)
print("Setelah disortir : ",arr1)
