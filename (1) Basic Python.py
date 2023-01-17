''' Variabel
1. Pengenal yang melibatkan huruf A-Z, a-z, digit 0-9, dan underscore (_)
2. Tidak boleh diawali dengan digit
3. lower case dan upper case berbeda sehingga nama dan NAMA berbeda
4. Tidak menggunakan keyword seperti for, while, dsb.
'''


''' Variabel dan Penugasan '''
a = 5 # a sebagai variabel 
#print(z) ini akan error karena z tidak terdefinisi/z belum diberikan tugas

a = "SIIUUUU"
print(a) # sekarang a berubah nilainya menjadi string SIIUUUU karena hal inilah python dikatakan tipe yang dinamis

x = 3
x = x + 7
print(x) # variabel x mewakili hasil dari nilai x yang lama ditambah dengan 7

# y = y + 8
# print(y) ini akan error NameError: name 'y' is not defined karena y belum di definisikan/belum diberikan tugas


''' Tipe Data 
    int = integer/bilangan bulat
    float = bilangan titik koma 
    complex = bilangan kompleks (diawali bilangan real dan diakhiri bilangan imajiner, misal 4+5j,7-9j)
    bin = bilangan biner (diawali 0b atau 0B, misal 0b1101101)
    okt = bilangan oktal (diawali 0o atau 0O, misal 0o29)
    hex = bilangan heksadesimal (diawali 0x atau 0X, misal 0x83,0xA)
'''
## Cara Mengecek Tipe Data
print(type(5))
print(type(0o5))
print(type(0x5))
print(type(13.5))
print(type(5 + 9j))
r = 9
print(type(r))
r = 9.0
print(type(r)) # float

## String
# String dibuat dengan tanda petik ganda atau tunggal (salah satu)

e = "Erick Thohir"
print(type(e))
f = 'Flawless'
print(type(f))

# String bisa saja tidak mengandung karakter apapun, dan disebut string kosong

h = " "
print(type(h))

i = ' '
print(type(i))

print('"selamat datang" lagi-lagi kata itu tidak sengaja terucap')

# Mengambil karakter di dalam string melalui indeks
tabun = "mungkin"
# Format -> variabel[start_indeks : end_indeks : step] -> default step adalah +1
# Indeks dimulai dari paling kiri yaitu 0,1,2,dst.. 
# Indeks paling kanan atau terakhir adalah -1
print(tabun[0]) # step default dan hanya menampilkan 1 karakter
print(tabun[0:4]) # dari indeks 0 - 3 (4 tidak termasuk)
print(tabun[-4:-2])
print(tabun[-3:-5:-1])

# Karakter Escape pada String
#     Karakter Escape adalah karakter yang diawali dengan \ 
#     \n = newline
#     \v = tab vertikal
#     \t = tab horizontal
#     \r = carriage return
#     \f = form feed

print("\vDear \nMila,")
print("\vDear \n\tMila,")


''' Ekspresi dan Operator 
    Suatu ekpresi melibatkan operator dan operand
'''
a = 7 + 8 - 9
# 7 + 8 - 9 adalah sebuah ekspresi yang disimpan didalam variabel a
# 7,8, dan 9 adalah operand. Sedangkan + dan - adalah operator.

## Operator Perpangkatan (**)
print(3**2, 2**4, 25**0.5)

## Operator Perkalian (*) dan Pembagian (/)
print(4*5,9*0, 0.5*4)
print(1/3, 8/2, 8/2.0) # selalu dikembalikan dalam bentuk float

## Operator Pembagian Bulat (//)
print(3//2, 1//2, 7//4.0) # 1//2 = 0.5 dan langsung dibulatkan kebawah menjadi 0

## Operator Modulo (%)
print(5%2, 2%3, 2%3.0) # mengembalikan sisa pembagian

## Operator Penjumlahan (+) dan Pengurangan (-)
print(4 + 2, 4.0 + 2, 5 - 3 , 5 - 3.0)


    # Latihan Konversi Satuan Waktu dari Detik ke Jam
    # Memanfaatkan Operator // dan %

total_detik = 20000

jumlah_jam = total_detik // 3600
jumlah_menit = (total_detik // 60) % 60
sisa_detik = total_detik % 60

print(jumlah_jam, "Jam")
print(jumlah_menit, "Menit")
print(sisa_detik, "Detik")


## Operator Penggabungan String

k = "kiri"
t = "to"
gabung = k + t
print(gabung)
blue = "wakatta" * 3
print(blue)

## Operator Pembanding 
#     >, lebih dari
#     <, kurang dari
#     >=, lebih dari sama dengan
#     <=, kurang dari sama dengan
#     ==, sama dengan
#     !=, tidak sama dengan

# Case Sensitive
print("Killua" == "KILLUA")
print("Killua" > "KILLUA")
print(5 >= 3)

## Operator Berbasis Bit 
#     &, dan untuk biner
#     |, atau untuk biner
#     ^, atau ekslusif (xor)
#     ~, inversi untuk biner
#     >>, geser kanan
#     <<, geser kiri


## Operator &
print(9 & 3) 
# Sifat biner dengan operator & dimana, 1 1 = 1 dan bentuk lain = 0 (akan true jika keduanya true)
# 1 0 0 1 -> 9
# 0 0 1 1 -> 3
# -------- &
# 0 0 0 1 -> 1

## Operator |
print(4 | 7) 
    # Sifat biner dengan operator | dimana 1 0, 0 1, atau 1 1 = 1 serta  0 0 = 0 (salah satu true atau keduanya true hasilnya true)
    # 0 1 0 0 -> 4
    # 0 1 0 1 -> 7
    # -------- |
    # 0 1 0 1 -> 7

## Operator ^
print(8 ^ 5) 
    # Sifat biner dengan operator ^ dimana 1 1 dan 0 0 = 0 sedangkan bentuk lain = 1 (akan false jika keduanya bernilai true atau false secara bersama-sama)
    # 1 0 0 0 -> 8
    # 0 1 0 1 -> 5
    # ------- ^
    # 1 1 0 1 -> 13

## Operator  ~ 
print(~10)
    # Sifat biner dengan operator ~ akan membalikkan masing-masing bit dari bit operand
    # 1 0 1 0 -> 10
    # -------- ~
    # 0 1 0 1 -> -11 (two's complement dimana ~operand = -operand - 1)

## Operator << dan >>
print(26 << 1) 
    # x << n == x * 2^n

print(26 >> 1) 
    # x >> n == x/2^n

## Operator Logika (and, or, not)
print((4 > 5) and (7 > 1)) 
    # Keduanya harus true agar hasilnya true
print((4 != 4) or (8<=9)) 
    # Salah satu atau keduanya true hasilnya true
print(not (10 >= 9))


''' Catatan tentang Ekspresi dan Penugasan '''
kaneki, oikawa, yuno = 10, 40, 90 
    # penugasan ini disebut penugasan paralel yang memiliki alamat yang berbeda
print("Nilai Awal Kaneki :", kaneki, "Nilai Awal Oikawa :", oikawa, "Nilai Awal Yuno :", yuno)

kaneki, oikawa, yuno = oikawa, yuno, kaneki 
    # cara ini bisa juga untuk swapping nilai
print("Nilai Akhir Kaneki :", kaneki, "Nilai Akhir Oikawa :", oikawa, "Nilai Akhir Yuno :", yuno)

p = q = r = 10
print(p,q,r)

p = 20
print(p,q,r)

# hati-hati bentuk diatas memiliki alamat yang sama dalam beberapa kasus jika salah satu variabel nilainya diganti 
# maka akan mengganti nilai ketiga variabel tersebut seperti kasus dibawah

x = y = z = [1]
print(x, y, z)

x.append(2)
print(x, y, z)

## Increment
alto = 9
alto += 1  # alto = alto + 1, penambahan 1
print(alto)

beta = 8
beta -= -1 # penambahan 1 juga dapat ditulis seperti ini
print(beta)

## Decrement
zeta = 16
zeta -= 1 # zeta = zeta - 1, pengurangan 1
print(zeta)

zepto = 34
zepto += -1 # pengurangan 1 juga dapat ditulis seperti ini
print(zepto)

## Bentuk *=, /=, //=, **=, dan %= memiliki prinsip yang sama dengan increment dan decrement

''' Memenggal Pernyataan Lebih Satu Baris '''
count = 4 + 6 -\
    4 # Memenggal pernyataan dengan tanda \ pada akhir baris, kalau mau dibuat dibaris selanjutnya
print(count) 

# Pada pernyataan yang pakai tanda kurung, tidak perlu pakai tanda \ untuk buat baris baru
bucket_list = ["atomic habit", "men are from mars women are from venus",
"the psychology of money"," the intellegent investor", "you do you"]
print(bucket_list)


''' Dua Pernyataan dalam Satu Baris (suites) '''
alarm = 8 ; print(alarm) # dipisahkan dengan tanda ;

''' Module '''
# misal mau pakai modul math untuk mencari akar kuadrat dari operand, kita harus impor modulnya dulu
import math
print(math.sqrt(169))


''' Built-in Function & Method '''
# Format -> Built-in Function -> nama_fungsi(argumen)
y = len("Hello World")
print(y)

# Format -> Method -> nama_variabel.nama_method(argumen,...)
x = [0]
x.append(1)
print(x)

s = "blackpearl"
print(s.upper())
