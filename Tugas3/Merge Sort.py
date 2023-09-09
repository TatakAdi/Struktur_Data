def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Mencari titik tengah array
        left_half = arr[:mid]  # Membagi array menjadi dua bagian
        right_half = arr[mid:]

        merge_sort(left_half)  # Memanggil merge_sort untuk setiap bagian
        merge_sort(right_half)

        i = j = k = 0  # Inisialisasi indeks untuk pengecekan dan penggabungan

        print("Menggabungkan: ", left_half, "dan", right_half)

        # Membandingkan dan menggabungkan kedua bagian
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menyalin sisa elemen jika ada
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print("Hasil sementara: ", arr)


# Contoh penggunaan:
arr = [12, 11, 13, 5, 6, 7]
print("Array awal: ", arr)
merge_sort(arr)
print("Hasil pengurutan:", arr)
