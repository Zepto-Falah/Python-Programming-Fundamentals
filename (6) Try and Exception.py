''' Error and Exception
    1. Syntax Error (penulisan kode tidak mengikuti kaidah yang benar)
    2. Runtime Error (error sewaktu eksekusi)
    3. Logic Error (kesalahan terdeteksi sewaktu skrip dieksekusi, tetapi tidak menghentikan eksekusi skrip)
'''

''' Jenis-Jenis Eksepsi
    AttributeError, FileNotFound, ImportError, IndexError, IOError, KeyboardInterrupt,
    KeyError, NameError, SyntaxError, TypeError, ValueError, dan ZeroDivisionError
'''
## IndexError
my_list = [0,1,2,3]
# print(my_list[5]) -> error karena index diluar jangkauan yang tersedia
print(my_list[3])

## FileNotFound
# f = open("Messi.txt", mode="r") -> error karena file Messi.txt tidak ada

## KeyboardInterrupt
# while 1: pass -> looping ini tidak akan berhenti kecuali jika menekan tombol ctrl+c

## KeyError
my_dictionary = {"Nol": 0, "Satu": 1, "Dua": 2}
# print(my_dictionary["dua"] keys "dua" tidak ada sehingga menyebabkan KeyError
print(my_dictionary["Nol"])

## NameError
a = 12
# print(b) hasilnya NameError karena variabel b belum didefinisikan
print(a)

## SyntaxError
# for i in range(2) 
#     print(i)
# Syntax akan error karena diakhir penulisan syntax for loop tidak ada tanda titik dua (:)
for i in range(2):
    print(i)

## TypeError -> error karena suatu operasi terhadap objek yang sebenarnya tidak didukung
my_tuple = (1,2,3)
# my_tuple[1] = 4 menyebabkan TypeError karena operasi seperti itu tidak dapat dilakukan pada tuple (immutable)
print(my_tuple)

## ValueError
my_string = "HELLO WORLD!"
# print(int(my_string)) menyebabkan ValueError karena value string tidak bisa dikonversi ke integer
print(my_string)

## ZeroDivisionError
a = 100
b = 0
# print(a/b) menyebabkan ZeroDivisionError karena suatu operand tidak boleh dibagi dengan 0
print(a/(b+2))

''' Menangani Eksepsi
    Untuk memberikan informasi yang jelas kepada user kenapa suatu program tidak dapat berjalan
    Format Penanganan Eksepsi:
    try:
        pernyataan_pernyataan
    except [nama_eksekpsi]: 
        pernyataan_pernyataan_dieksekusi_jika_eksepsi_ada
    [else:
        pernyataan_pernyataan_dieksekusi_jika_tidak_ada_eksepsi]
'''
## Implementasi 
def division(numerator, denominator):
    try:
        print("Division Result =",numerator/denominator)
    except: 
        # Bagian except diatas akan dijalankan jika terjadi eksepsi apa saja
        # Namun, kadang kita tidak ingin semua eksepsi ditangani seperti MemoryError
        # Jadi lebih baik menuliskan nama eksepsi yang ingin ditangani
        print("Denominator cannot be 0")
    else: # Else dapat tidak ditulis
        print("Division is succesful!")
division(60,12)
division(100,0) # Eksepsi akan ditangani


while True:
    try:
        bilangan = input("Masukkan bilangan :")
        bilangan = int(bilangan)
        break
    except ValueError:
        print("Bilangan yang anda masukkan salah")
print("Anda memasukkan bilangan =", bilangan)
    

## Menangani Lebih dari Satu Eksepsi 
# Satu try dengan lebih dari 1 execpt dapat dimanfaatkan jika ada beberapa eksepsi yang ingin ditangani
while True:
    try:
        bilangan = input("Masukkan bilangan :")
        bilangan = int(bilangan)
        break
    except ValueError:
        print("Bilangan yang anda masukkan salah")
    except KeyboardInterrupt:
        print("\nMaaf jangan menenkan tombol Ctrl+C")
print("Anda memasukkan bilangan =", bilangan)


## Satu except dengan Lebih dari Satu Eksepsi
def bil_bulat(n):
    try:
        return int(n)
    except (TypeError, ValueError): 
        # Cara diatas dapat digunakan jika perlakuan yang dikenakan terhadap beberapa eksepsi sama
        return None
    
print(bil_bulat(12))
print(bil_bulat([1,2,3]))

''' Melontarkan Eksepsi
    Melontarkan pesan kesalahan di sebuah eksepsi dengan raise
'''
class kesalahanku(Exception): # Kelas eksepsi
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise kesalahanku(3)
except kesalahanku as error:
    print("Eksepsi Terjadi, Value:", error.value)


''' Pernyataan Assert
    Melontarkan eksepsi bisa digunakan untuk debugging (mencari kesalahan)
'''
def fx(a,b):
    if __debug__:
        if b == 0:
            raise AssertionError("Argumen kedua tak boleh 0")
    return (a,b)
print(fx(1,2))
# print(fx(1,0))

def gx(a,b):
    assert b != 0, ("Argumen kedua tak boleh 0")
print(fx(1,2))
# print(fx(1,0))

''' Pernyataan try...finally
    try...finally menjamin eksekusi terhadap suatu perintah tidak tergantung
    oleh terjadi atau tidaknya eksepsi. Hal ini berguna untuk melakukan tindakan
    seperti menutup file yang telah dibuka
'''
def px(a):
    try:
        print(1/a)
    finally:
        print("Bagian ini pasti dijalankan")
        # Bagian ini pasti dijalankan karena tidak tergantung oleh terjadi atau tidaknya eksepsi

px(4)
# px(0)
