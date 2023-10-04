def hitung_jumlah_list(my_list):
    
    total = 0
    for elemen in my_list:
        total += elemen
    return total

# contoh penggunaan
list_angka = [1, 2, 3, 4, 5]
jumlah = hitung_jumlah_list(list_angka)
print("Jumlah semua elemen dalam list:", jumlah)
