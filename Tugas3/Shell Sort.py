def Shell_sort(arr):
    n = len(arr)
    jarak = n // 2

    while jarak > 0:
        j = jarak
        while j < n:
            i = j-jarak
            while i >=0:
                if arr[i+jarak] > arr[i]:
                    break
                else:
                    arr[i+jarak],arr[i]=arr[i],arr[i+jarak]
                
                i -= jarak
            j += 1
        jarak //= 2

array = [12,34,54,2,3]
print("input array: ", array)
Shell_sort(array)
print("Sorted array: ", array)