def selection_sort (array):
    for index in range (len(array)):
        min_index = index
        for j in range (index +1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        print("Value yang ditukar : {} dengan {}".format(array[index],array[min_index]))
        array[index],array[min_index] = array[min_index], array[index]
        print(array)

arr = [10,50,4,6,7,10,47,20]
selection_sort(arr)
print(arr)