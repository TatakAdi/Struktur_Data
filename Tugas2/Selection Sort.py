def selection_sort (array):
    for i in range (len(array)):
        min_index = i
        #Menemukan elemen terkecil dari array yang belum terurutkan
        for j in range (i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        
        #Menukar value dalam array dengan selection sort
        print("Value yang ditukar : {} dengan {}".format(array[i],array[min_index]))
        array[i],array[min_index] = array[min_index], array[i]
        print(array)

arr = [10,50,4,6,7,10,47,20]
selection_sort(arr)
print(arr)