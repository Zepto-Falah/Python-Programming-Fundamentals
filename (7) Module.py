''' Module and Import Module
    Modul atau pustaka adalah suatu file yang berisi kumpulan kelas, fungsi, dan prosedur
    yang bisa diakses dalam mode interaktif. Modul harus diimpor dulu agar bisa digunakan

    Format:
    import [modul]
    atau
    import [modul_1, modul_2, modul_3]
'''
import math
import cmath, numpy, time

''' Melihat Isi Modul
    Isi suatu modul dapat dilihat dengan menggunakan fungsi dir()

    Format:
    dir(modul)
'''
# print(dir(math))
# print(dir(cmath))
# print(dir(numpy))
# print(dir(time))

# help(cmath) # Untuk memperoleh dokumentasi dari suatu modul (modul diimpor dulu modulnya)


''' Membuat Module
    Modul yang dibuat harus berada di dalam 1 folder yang sama dengan file code yang digunakan
    agar dapat dipanggil. Jika berada di folder yang berbeda maka kita harus memberi tau letak
    modulnya dengan import sys -> sys.path.append("Letak modul/filenya")
'''
## Modul yang Terletak di dalam 1 Folder yang Sama dengan File Code
import Contoh_Module
print(Contoh_Module.villain)
print(Contoh_Module.all_villains())

## Modul yang Terletak di Folder yang Berbeda dengan File Code
import sys
sys.path.append(r"C:\Users\user\OneDrive\Documents\SEMESTER 1 (117)\Python\Practice Python\Example Module")
print(sys.path)
import my_module
# Mengimpor my_module agar bisa memanfaatkan euclid algorithm pada modul tersebut
# Untuk mencari greatest common divisor dari 2 buah bilangan
print(my_module.euclid(16,12)) 

''' Mengetahui Modul-Modul yang Sudah Dibuat
    Dengan mengimpor modul sys lalu print(sys.modules)
'''
import sys
# print(sys.modules)

''' Membebaskan Memori Modul
    Jika sudah selesai menggunakan modul dan tidak memerlukannya lagi,
    kita bisa membebaskan memori yang digunakan oleh modul dengan pernyataan del

    Format:
    del [nama_modul]
'''

# import sys, os
# print(os.name)
# del os
# del sys.modules["os"] # Referensi modul juga perlu dihapus
# # print(os.name) modul sudah terhapus


''' Package (Paket)
    Modul-modul yang berkaitan erat umumnya dikemas dalam sebuah paket (Package)
'''
# import sys
# sys.path.append("C:\Users\user\OneDrive\Documents\SEMESTER 1 (117)\Python\Practice Python\Dasar Pemrograman Python 3")
# import Paketku