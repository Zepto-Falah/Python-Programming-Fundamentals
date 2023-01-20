''' Kedudukan Fungsi dalam Python 
    Biasanya fungsi dipanggil untuk mengurangi duplikasi kode
    Atau untuk membuat suatu program agar dapat dipecah menjadi sejumlah bagian agar lebih mudah dikelola
'''

''' Mendefinisikan Fungsi 
    Format:
    def nama_fungsi(argumen1, argumen2,...):
        "string dokumentasi" -> opsional
        pernyataan_pernyataan
        [return nilai_balik_yang_diinginkan]
'''
def max_value(x,y): 
    "Memperoleh nilai terbesar dari bilangan x dan y" # String Dokumentasi
    if x > y:
        return x
    else:
        return y
print(max_value(5,8)) 

## Fungsi bisa Saja tanpa Argumen
def gojo_satoru(): return "Jujutsu Kaisen"
print(gojo_satoru())

# Untuk Mengetahui String Dokumentasi Gunakan Format namafungsi.__doc__
print(max_value.__doc__)

''' Argumen dengan Objek Mutable dan Immutable '''
## Pada Objek Mutable seperti List
anime = ["AOT", "Haikyuu", "Black Clover", "My Hero Acamedia!"]

def series_anime(arg):
    arg[0] = "The Eminence in Shadow"
    # arg[0:2] = "HunterxHunter", "Tokyo Ghoul"
    # arg[0:3] = "Sword Art Online", "Kuroko no Basket"
    print("List di fungsi :", arg)

series_anime(anime)
print("List awal :", anime)
# Di atas terlihat bahwa list awal mengalami perubahan karena objeknya mutable

## Pada Objek Immutable seperti Integer
my_number = 100
def number(arg):
    arg = 30
    print("Angka di fungsi :", arg)

number(my_number)
print("Angka awal :", my_number) 
# Di atas terlihat bahwa angka awal tidak mengalami perubahan karena objeknya immutable

''' Argumen Bernama '''
def jadwal_les(x,y,z):
    print(x,y,z)

jadwal_les(x= "Senin", y= "Kamis", z= "Jumat")
jadwal_les("Selasa", "Rabu", "Sabtu")

''' Argumen Bawaan 
    Argumen bawaan memungkinkaan suatu argumen boleh tidak ditulis ketika dipanggil 
    Hal ini karena nilai argumen sudah diisi
'''
def ace(kata, jumlah = 3):
    return kata*jumlah

print(ace("Mars-Venus"))
print(ace("Compound Interest", 2)) # argumen 2 akan dieksekusi


''' Argumen Berbentuk *arg 
    *arg berguna untuk memperoleh keseluruhan argumen dalam fungsi bentuk tuple
'''
def tampilanarg(*arg): print(arg)
tampilanarg(9,8,7,6)

def bigger(*arg):
    maks_value = arg[0]
    for value in arg[1:]:
        if value > maks_value:
            maks_value = value
    return maks_value

print(bigger(2,5))
print(bigger(45,23,213,213))
print(bigger(8,10,1203,23,912,9283))
# Fungsi diatas dapat memuat jumlah argumen yang bervariasi dengan menggunakan *arg

''' Fungsi Tanpa Return '''
def tanpa_return(): pass
print(tanpa_return()) # Tidak melakukan apapun


''' Fungsi dengan Argumen Berbentuk **arg 
    Fungsi dengan argumen berbentuk **arg bisa dipakai untuk memperoleh struktur data berjenis dictionary
'''
def perolehdict(**arg):
    return arg

print(perolehdict(Jujutsu_Kaisen = "Itadori Yuji",Black_Clover = "Asta"))

''' Penugasan Fungsi dan Fungsi Sebagai Argumen '''
def my_func(fungsi, nilai):
    return fungsi(nilai) # fungsi sebagai argumen

print(my_func(len, "Blacklist"))

def my_arg(fungsi, *arg): # Kalau mau pakai banyak parameter bisa pake *arg
    return fungsi(arg)
print(my_arg(list, 4, 5, 6, 7 ,8))
print(my_arg(len, 1, 2 ,3 ,4 ,5 ,6, 7))
# print(my_arg(float, 1, 2 ,3 ,4 ,5 ,6, 7)) # ini akan error karna struktur data berbentuk tuple
print(my_arg(min, 1, 2 ,3 ,4 ,5 ,6, 7))


''' Lingkup Variabel 
    Variabel Global
    -> Bisa diakses pada semua bagian skrip yang sedang digunakan, termasuk dalam seluruh fungsi
    -> Daur hidupnya selama skrip dieksekusi

    Variabel Lokal
    -> Hanya dikenal dalam fungsi tempat variabel tersebut didefinisikan
    -> Daur hidupnya adalah saat fungsi dipanggil hingga eksekusi fungsi tersebut berakhir
'''
## Kalau kita menunjuk suatu variabel, python akan otomatis mencari variabel lokal dulu baru variabel global
## Kalau tidak ada python akan membalikkan NameError

variabel_alpha = "Echo" # Variabel Global
def mlbb_team():
    print("Team 1 :", variabel_alpha) # Variabel Global diatas juga dikenal didalam fungsi mlbb_team
    variabel_beta = "BTR" # Variabel Lokal bagi fungsi mlbb_team
    print("Team 2 :", variabel_beta)

mlbb_team()
# print(variabel_beta) # variabel beta tidak dikenali di luar fungsi karena bersifat lokal

number = 12
def my_num():
    number = 20 # Bersifat lokal
    print("Number di dalam fungsi :", number)

my_num()
print("Number di luar fungsi (var_global) :", number)
# Nilai variabel global number dapat dilihat di dalam fungsi, tapi isinya tidak dapat berubah di luar fungsi


## Mengubah Nilai Variabel Global di dalam Fungsi
chairs = 12
def my_chairs():
    global chairs # Perubahan bersifat global
    chairs = 20
    print("Chairs di dalam fungsi :", chairs)

my_chairs()
print("Chairs di luar fungsi (diubah dengan keyword global) :", chairs)


''' Fungsi Tak Bernama 
    Format -> lambda [arg1, arg2, ...] : ekspresi
'''
f = lambda x,y : x + y
print(f(4,5))

g = lambda fungsi,*arg : fungsi(*arg)
print(g(len,"Ultra Instinct"))


''' Recursion Function 
    Mekanisme dimana fungsi dapat digunaka untuk memanggil dirinya sendiri (fungsi rekursif)
'''
# Mencari nilai faktorial suatu bilangan
def faktorial(n):
    if (n==0) or (n==1):
        return 1
    else: 
        return n*faktorial(n-1)
print(faktorial(5))

# Mencari greatest common divisor dari dua buah bilangan
def euclid_algorithm(a,b):
    if (b==0):
        return a
    else:
        return euclid_algorithm(b, a%b)
print(euclid_algorithm(4,10))

# Fungsi rekusif menggunakan if...else...statement dengan return 

print(__builtins__)


''' Latihan 
    Membuat Program Konversi Suhu dari Celcius ke Fahrenheit dan Sebaliknya dengan Memanfaatkan function
'''
 
def celcius_to_fahrenheit():
    celcius = int(input("Masukkan Suhu (Celcius) : "))
    fahrenheit = (9/5)*celcius +32
    print("Suhu =", fahrenheit, "Fahrenheit")

def fahrenheit_to_celcius():
    fahrenheit = int(input("Masukkan Suhu (Fahrenheit) : "))
    celcius = (5/9)*(fahrenheit - 32)
    print("Suhu =", celcius, "Celcius")

print("\n","="*5, "Program Konversi Suhu Sederhana", "="*5,"\n")
print("Pilihan :")
print("1. Konversi Suhu dari Celcius Ke Fahrenheit")
print("2. Konversi Suhu dari Fahrenheit Ke Celsius", "\n")

opsi = int(input("Masukkan pilihan Anda : "))
if opsi == 1:
    celcius_to_fahrenheit()
elif opsi == 2:
    fahrenheit_to_celcius()
else:
    print("Mohon pilih antara 1 atau 2")

def tulis():
    i = 1
    while i < 5:
        print(i)
        i += 1

print(tulis())

def balik(st):
    if st != "":
        balik(st[1:])
        print(st[0])

print(balik("Python"))