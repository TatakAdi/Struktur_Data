def shellSort(array, n):
    step = 1
    while step < n // 3:
        step = step * 3 + 1

    while step >= 1:
        print(f"Step {step} : {array}")  
        for i in range(step, n):
            temp = array[i]
            j = i
            while j >= step and array[j - step] > temp:
                array[j] = array[j - step]
                j -= step
                if array[j] != temp:
                    print(f"{temp} <--> {array[j]}")
            array[j] = temp
            print(f"Step {step} : {array}")
        step //= 3


data = [10,1,7,18,29,5,10,23,17,33,4,12,8]
size = len(data)
print('Sebelum sorting:')
print(data)
shellSort(data, size)
print('Setelah sorting:')
print(data)
