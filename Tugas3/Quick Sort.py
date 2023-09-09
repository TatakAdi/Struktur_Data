def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Pilih elemen pivot (tengah dari array dalam kasus ini)
    left = [x for x in arr if x < pivot]  # Elemen yang lebih kecil dari pivot
    middle = [x for x in arr if x == pivot]  # Elemen yang sama dengan pivot
    right = [x for x in arr if x > pivot]  # Elemen yang lebih besar dari pivot

    # Gabungkan dan cetak setiap langkah penukaran
    sorted_arr = quick_sort(left) + middle + quick_sort(right)
    print(f"Step: {arr} -> {sorted_arr}")

    return sorted_arr


# Contoh penggunaan:
my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quick_sort(my_list)
print("Hasil akhir:", sorted_list)
