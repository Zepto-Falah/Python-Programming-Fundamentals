''' Pernyataan if, while, dan for'''

''' Indentasi 
    adalah penulisan pernyataan yang menjorok ke kanan
    Indentasi umunya terdiri atas 4 spasi
'''

x, y = 3, 2
if x > y:
    print("Yes") # pernyataan ini diletakkan menjorok ke kanan (menggunakan indentasi)


''' if...elif...else... statement '''

## Format
# if kondisi_1:
#   pernyataan_pernyataan_1
# [elif kondisi_2:
#   pernyataan_pernyataan_2]
# [elif kondisi_3:
#   pernyataan_pernyataan_3]
#  ...
# [else:
#   pernyataan_pernyataan_n]

# Tanda [] artinya bagian itu boleh ada atau pun tidak

## if Statement Sederhana
upper_bracket = "RRQ", "EVOS", "ONIC"

if "EVOS" in upper_bracket:
    print("EVOS kweereen!")

if "evos" in upper_bracket: # case sensitive
    print("evos rawwrr!")

mila = 100
violet = 70
bigger = violet

if bigger < mila:
    bigger = mila
    print("Bilangan terbesar :", bigger)

# if statement sederhana juga dapat ditulis menjadi 1 line
# Format -> if kondisi: pernyataan
if mila == 100: print("The moon is beautiful, isn't it?")

## if...else... statement
nilai_ujian = int(input("Masukkan nilai ujian matematika (0-100) :"))

if nilai_ujian >= 70:
    print("Selamat kamu lulus!")
else:
    print("Maaf, kamu tidak lulus")

## if...elif...else statement
jumlah_shoot = int(input("Jumlah shoot masuk ke ring dalam 1 menit :"))

if jumlah_shoot >= 30:
    print("A")
elif 20 <= jumlah_shoot < 30:
    print("B")
elif 15 <= jumlah_shoot < 20:
    print("C")
else:
    print("D")

''' for Statement '''

## Format
# for variabel in list:
#   pernyataan_pernyataan_1
# [else:
#   pernyataan_pernyataan_2]

# Bagian di dalam tanda [] akan dieksekusi paling akhir setelah for loop selesai
# Bagian di dalam tanda [] juga boleh tidak digunakan

for violet in [9, 0, 2, 1]:
    print(violet)
# pada iterasi pertama, violet = 9
# pada iterasi kedua, violet = 0
# dst...

for mikasa in "Attack on Titan":
    print(mikasa)

for cid in "The Eminence in Shadow":
    print(cid, end=" ") 
# ingat end= akan membuat akhir baris tanpa newline 
# dan end= " " akan membuat setiap pernyataan dipisahkan dengan spasi


''' while Statement '''
## Format
# while kondisi:
#   pernyataan_pernyataan_1
# [else:
#   pernyataan_pernyataan_2]

# pernyataan_pernyataan_1 akan dieksekusi terus-menerus sepanjang kondisinya benar
# pernyataan_pernyataan_2 dieksekusi terakhir tepat sebelum while loop berakhir dan tidak wajib digunakan

attempt = 0
while attempt <= 3:
    print("Attempt sudah digunakan sebanyak =", attempt, "kali")
    attempt += 1
else:
    print("Attempt sudah mencapai limit harian")

## Latihan Membuat Segitiga Bintang
tinggi_segitiga = int(input("Masukkan tinggi segitiga :"))
baris = 1

while baris <= tinggi_segitiga:
    print("*"*baris)
    baris +=1

''' Looping Yang Tidak Pernah Berakhir '''

# while True:
#     print("Infinity")
# looping di atas tidak pernah berakhir karena while loop akan melooping secara terus-menerus selama kondisinya benar
# untuk menghentikan while loop kita harus membuat kondisi dimana dia harus berhenti melooping

''' Break Statement '''
for i in range(9): # looping dimulai dari 0-8 (9 tidak termasuk)
    print(i)
    if i == 4: 
        break # disini looping yang harusnya sampai 8 akan dihentikan sampai 3

else:
    print("Looping berakhir") # pernyataan break di atas membuat bagian else statement disini tidak dieksekusi
# break statement seperti ini juga berlaku pada while loop

## Latihan Break Statement
# Mencari Penggalan Nama Laptop Acer

nama_laptop = ["Acer Aspire 3", "Acer Nitro 5", "Acer Swift X","Acer Aspire 5", 
                "Acer Predator Helios 300", "Acer Predator Helios 500"]

nama_laptop_yang_dicari = input("Masukkan penggalan nama laptop acer :")
indeks = 0

ditemukan = False # Boolean sebagai flag kita atur dulu belum ada/false
while indeks < len(nama_laptop):
    if nama_laptop_yang_dicari.lower() in nama_laptop[indeks].lower():
        ditemukan = True # karena nama laptop yang dicari sudah ditemukan berarti kita tandai/beri flag dengan boolean True
        break
    indeks -= -1 # increment 1

if ditemukan:
    print("Nama laptop yang Anda cari cocok dengan :", nama_laptop[indeks])
else:
    print("Nama laptop yang Anda cari tidak ditemukan")


''' continue Statement '''

## Pernyataan ini berfungsi untuk mengabaikan sisa pernyataan dalam blok kode
for i in range(6):
    if i == 4:
        continue
    print(i)

else:
    print("Akhir dari for loop")


''' pass Statement '''

## Pernyataan ini berarti "tidak melakukan apa-apa"
for j in range(0,9,1): # range(start,end,step), dimana end tidak termasuk dan default start adalah 0
    print(j)
    if j > 6:
        pass


''' Latihan '''
## Menyusun Data Perpangkatan dengan for loop
n = int(input("Masukkan jumlah baris :"))
for i in range((2*n)+1):
    if i != 0:
        if i % 2 == 0:
            print(i, i**2)

## Menyusun Data Perpangkatan dengan while loop
inp = int(input("Masukkan jumlah baris :"))
j = 2
while j <= 2*inp:
    print(j, j*j)
    j += 2

## Membuat Piramida Bintang
inp_user = int(input("Masukkan alas piramida bintang :"))
spasi = int(inp_user/2)
# print(spasi)
for i in range(inp_user+1):
    if (i % 2) != 0: 
        print(" "*spasi,"*"*i)
        spasi -= 1

## Menghitung Penjumlahan Bilangan Genap dari 2-40
# print("="*40)
count = 0
for i in range(2,41,2):
    count += i
print(count)

## Mencari Karakter yang Berupa Huruf Kapital dalam Suatu Kalimat dan Menghitung Jumlah Huruf Kapitalnya
kalimat = input("Masukkan kalimat yang mengandung lower case dan upper case s:")
count = 0
result = []

for i in kalimat:
    if (i == " ") or (i == ",") or (i == ".") or (i =="<")\
        or (i == ">") or (i == "/") or (i == "?") or (i == ";") or (i == "'")\
        or (i == ":") or (i == "[") or (i == "]") or (i == "{") or (i == "}")\
        or (i == "\ ") or (i =="|") or (i == "`") or (i == "~") or (i == "1")\
        or (i == "2") or (i == "3") or (i == "4") or (i == "5 ") or (i =="6")\
        or (i == "7") or (i == "8") or (i == "9") or (i == "0") or (i == "!")\
        or (i == "@") or (i == "#") or (i =="$") or (i == "%") or (i == "^")\
        or (i == "&") or (i == "*") or (i == "(") or (i == ")") or (i == "_ ")\
        or (i =="+") or (i == "-") or (i == "="):
        del i
    elif i == i.upper():
        result.append(i)
        count += 1

print("Huruf kapital yang terdapat di dalam kalimat =",*result)
print("Banyaknya huruf kapital yang terkandung dalam kalimat =", count)