''' Struktur Data
    adalah suatu objek yang dapat menyimpan sejumlah data yaitu list, tuple, dan dictionary
'''

''' List 
    Ditulis dengan tanda kurung siku ([]), antar-elemen dipisah dengan koma (,)
'''

## Menugaskan List dan Menampilkan List
asterix = [1, "Infinix", True, 2.3, " "] # Bisa menyimpan berbagai jenis tipe data
print(asterix)

chrollo = ["Blackjack",["Nova", "Luminair"], 12, False]
print(chrollo)
# List bisa mengandung elemen berupa list juga (nested list)

## Mengakses Elemen List dengan Indeks
# Format -> variabel_list[indeks]
mila = [71, 81, 91]
print(mila[0]) # Mengakses elemen list pada indeks 0
print(mila[1:]) # Jika elemen yang dipanggil lebih dari 1 maka akan dikembalikan dalam bentuk list
print(*mila[1:]) # Gunakan tanda * agar dikembalikan dalam bentuk bilangan saja

# Format Nested List -> variabel_list[indeks][indeks_nested_list]
science = ['math', 'chemistry', ["The King of Science", "The Queen of Science"]]
print(science[-1][1])

## Mengubah Data List
haikyuu = ["Kageyama Tobio", "Miya Osamu", "Oikawa Tooru", "Hinata Shoyo"]
haikyuu[1] = "Kotaro Bokuto"
print(haikyuu)

haikyuu[2:] = "Wakatoshi Ushijima", "Yu Nishinoya"
print(haikyuu)

## Mengetahui Jumlah Elemen List
# Format -> len(variabel_list)
black_clover = [["Asta", "Yuno"], "Yami Sukehiro", "Luck Voltia"]
print("Banyaknya jumlah elemen pada list Black Clover :", len(black_clover))

## Menghapus Elemen List
# Format -> del variabel_list[indeks]
jujutsu_kaisen = ["Itadori Yuji", "Megumi Fushiguro", "Nobara Kugisaki", "Gojo Satoru", "Geto Suguru"]
del jujutsu_kaisen[-1] # del menggunakan indeks untuk menghapus
print(jujutsu_kaisen)

# Format -> variabel_list.remove(elemen)
jujutsu_kaisen.remove("Itadori Yuji") # Case Sensitive, remove harus menunjuk nama elemen untuk menghapus
print(jujutsu_kaisen)

# Format -> variabel_list.pop(indeks)
jujutsu_kaisen.pop() # pop() defaultnya menghapus elemen terakhir
print(jujutsu_kaisen)

jujutsu_kaisen.pop(1)
print(jujutsu_kaisen)

## Menambah Elemen List
# Format -> variabel_list.append(elemen)
bluebird = [9, "Januari", 2001]
bluebird.append("Celestial") # append menambahkan elemen di akhir list
print(bluebird)

# Format -> variabel_list.insert(indeks, elemen)
bluebird.insert(-1, "Mila") # Mila akan disisipkan setelah 2001 karena list bluebird berakhir di 2001
print(bluebird)

## Method Lain
# Method count(x) -> menghitung frekuensi x pada list
bilangan_genap = [2, 8, 10 , 24, 12, 2, 22, 20, 24, 2, 8, 10]
print(bilangan_genap.count(2))

# Method extend(d) -> menambahkan list d ke dalam list
bilangan_float = [2.0, 4.0, 8.0]
bilangan_genap.extend(bilangan_float)
print(bilangan_genap) 
# Bentuk print(bilangan_genap.extend(bilangan_float)) akan menghasilkan None

# Method index(x) -> mencari indeks dari x pertama yang dijumpai di list
print(bilangan_genap.index(2)) 
print(bilangan_genap.index(2.0)) 

# Method reverse() -> membalikkan urutan elemen pada list
abjad = ["a", "b", "c", "d", "e"]
print(abjad.reverse()) # Mengembalikkan None
print(abjad)

# Method sort() -> mengurutkan elemen pada list
abjad.sort() # Default pengurutan secara ascending
print(abjad)

angka = [1, 4, 3, 5, 7, 6, 2]
angka.sort(reverse=True) # Diurutkan secara descending
print(angka) 

nama_murid = ["nova", "Narnia", "killa", "Alfa", "beta"]
nama_murid.sort(key=str.lower) 
# key=str.lower untuk mengurutkan tanpa membedakan lower case dengan upper case
print(nama_murid)

# Built-in Function sorted() -> membuat list baru yang sudah diurutkan
goku = [2, 3, 1, 9, 7] # List lama
sorted(goku) # List baru
print(goku) # Bentuk ini menampilkan list lama (jadi list lama tidak berubah)
print(sorted(goku)) # Bentuk ini adalah list baru yang sudah terurut

## Built-in Function range()
# list(range()) -> membuat list dengan elemen bertipe integer
# Format -> range(start, end, step) dimana end tidak termasuk
number = list(range(2,10))
print(number)

number = list(range(10))
print(number)

number = list(range(1,10,2))
print(number)

number = list(range(10,-10,-2))
print(number)

## Built-in Function filter()
# filter() -> memfilter suatu list melalui suatu fungsi yang didefinisikan pemakai
# format -> list(filter(fungsi, list))

# Implementasi pada Tipe Data Integer
def fungsi(x): return x % 2 == 0
print(list(filter(fungsi, range(1,10))))

# Implementasi pada Tipe Data String
def uppercase(x): return (x >= "A") and (x <= "Z") # Mereturn upper case
print(list(filter(uppercase, "ProMiNEnce")))


## Built-in Function map()
# Format -> list(map(fungsi, list))
# Format diatas untuk membuat list dari suatu list dengan setiap elemen yang dikenakan operasi suatu fungsi
def rasio(x): return 1/x
print(list(map(rasio, [2, 10, 50])))

print(list(map(int, [2.9, 12.4, 10.5])))

## Built-in Function sum()
# Format -> sum(list)
print(sum([1,2,3,4]))

## Built-in Function min()
# Format -> min(list)
print(min([10, 0, 12, -1]))

## Built-in Function max()
# Format -> max(list)
print(max([10, 0, 12, -1]))


''' Tuple 
    Tuple menyerupai list, ditulis dengan tanda kurung bulat (), antar-elemen dipisah dengan koma (,)
    Struktur data ini bersifat immutable (bagian isinya tidak dapat diubah)
'''
## Mengetahui Jumlah Elemen Tuple
xenon = (1,2,3)
print(len(xenon))

## Mengakses Elemen Tuple
print(xenon[0])
print(xenon[:2]) # Terlihat jika irisan digunakan hasilnya berupa tuple

## Operator pada Tuple
# Semua operator yang dapat diterapkan pada list bisa diterapkan juga pada tuple
yelena = (4,5,6)
print(yelena + (7,8,9))

## Fungsi dengan Nilai Balik Berupa Tuple
def resultuple():
    return (12, "Octopus", "Ryota")

print(resultuple())

## Konversi dari List ke Tuple dan Sebaliknya
# Format list ke tuple -> tuple(list)
my_list = [9,8,7]
my_tuple = tuple(my_list)
print(my_tuple)

# Format tuple ke list -> list(tuple)
new_tuple = (12,21)
new_list = list(new_tuple)
print(new_list)

## Memperoleh Tuple yang Berurutan
customer = ("Rin", "Mila", "Violet")
print(sorted(customer)) # Hasil sorted() adalah list
print(tuple(sorted(customer))) # Jika ingin hasilnya dalam tuple

''' Dictionary
    Di dalam dictionary terdapat keys untuk mencari suatu values
    Format -> variabel = {keys1: values1, keys2: values2,...}
    Sebuah elemen dalam dictionary selalu berupa pasangan keys dan values
    keys bisa berupa tipe data immutable dan values bisa berupa tipe data apa saja
'''
## Memperoleh Values Melalui Keys
# Format -> variabel[kunci]
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
print(my_dictionary["Hewan"]) 
print(my_dictionary["Buah"]) # Case sensitive

## Mengetahui Jumlah Keys
print(len(my_dictionary))

## Memperoleh Daftar Keys 
# Format -> variabel.keys()
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
print(my_dictionary.keys())
print(tuple(my_dictionary.keys()))
print(list(my_dictionary.keys()))

## Memperoleh Daftar Values
# Format -> variabel.values()
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
print(my_dictionary.values())
print(tuple(my_dictionary.values()))
print(list(my_dictionary.values()))

## Memperoleh Pasangan Keys dan Values
# Format -> variabel.items()
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
print(my_dictionary.items())
print(tuple(my_dictionary.items()))
print(list(my_dictionary.items()))

## Memperoleh Values dan Keys Melalui Indeks
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
thorfin = tuple(my_dictionary.items())
# Values
print(thorfin[0][1]) 
print(thorfin[1][1])
# Keys
print(thorfin[0][0]) 
print(thorfin[1][0])

my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
for keys, values in my_dictionary.items(): # Enumerate for loop dengan 2 parameter yaitu keys dan values
    print("%-10s %-10s" % (keys, values))

## Memeriksa Keberadaan Values
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
print("Mobil" in my_dictionary)

## Memperoleh Values dengan Method get()
print(my_dictionary.get("Hewan")) # get(keys)
print(my_dictionary.get("Mobil")) # Hasil none karena tidak ada keys Mobil

print(my_dictionary.get("Mobil", "Tak ada")) # Hasilnya berupa 'Tak ada' karena keys tidak ada dan diformat "Tak Ada"
print(my_dictionary.get("Buah", "Tak ada")) # Kalau keys ada maka "Tak Ada" tidak akan dieksekusi

## Mengubah Values Data dengan  Method update()
# Cara 1
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
my_dictionary.update({"Hewan": "Naga"}) # Case sensitive
print(my_dictionary)

# Cara 2
my_dictionary["Buah"] = "Anggur"
print(my_dictionary)

## Menambah Data dengan Methode update()
# Jika pasangan keys dan values tidak ada di dictionary maka method update() akan otomatis menambahkan keys dan values
# Cara 1
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
my_dictionary.update({"Buku": "Men are From Mars Women are From Venus"})
print(my_dictionary)

# Cara 2
my_dictionary["Black Clover"] = "Langris"
print(my_dictionary)

## Menyalin Dictionary dengan copy()
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
d = my_dictionary # Cara ini berarti mereferensikan d ke my_dictionary (tidak mengcopy)

my_dictionary["Black Clover"] = "Yuno"
print(my_dictionary)
print(d)

my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
d = my_dictionary.copy() # Cara ini berarti menyalin my_dictionary

my_dictionary["Black Clover"] = "Yuno"
print(my_dictionary)
print(d) # Perubahan pada my_dictionary tidak berpengaruh pada d

## Menghapus Data dengan Fungsi del()
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
del(my_dictionary["Hewan"])
print(my_dictionary)

## Menghapus Semua Data dengan Method clear()
my_dictionary = {"Hewan": "Kucing", "Buah": "Pisang"}
my_dictionary.clear()
print(my_dictionary)

## Menghapus dengan Method popitem()
uchiha = {"Itachi": 28, "Madara": 45, "Sasuke": 20}
uchiha.popitem() # Menghapus elemen terakhir
print(uchiha)

## Memproses Item melalui  Looping
uchiha = {"Itachi": 28, "Madara": 45, "Sasuke": 20}
for keys in uchiha:
    print(keys)

for keys in uchiha:
    print(keys, uchiha[keys])

## Membuat Dicitonary dari Suatu List dengan Method fromkeys()
# Format -> {}.fromkeys(list, values)
abjad = {}.fromkeys(["a", "b", "c", "d"], 0) 
print(abjad)
# fromkeys() hanya bisa membuat dictionary dengan values yang sama bagi setiap keys

## Menggunakan Method setdefault()
# setdefault() untuk mengambil values berdasarkan keys yang dicari
# Jika keys yang dicari tidak ada maka akan otomatis ditambahkan ke dictionary
uchiha = {"Itachi": 28, "Madara": 45, "Sasuke": 20}
print(uchiha.setdefault("Sasuke", "Tak ada"))
print(uchiha)

print(uchiha.setdefault("Shishui", "Tak ada")) # Ketika suatu keys tidak ada dan langsung ditambahkan di akhir dictionary
print(uchiha)


## Operator pada Dictionary
# Operator pembandingan (>=, ==, !=, dsb..) dan in
uchiha = {"Itachi": 28, "Madara": 45, "Sasuke": 20}
print("Cid" in uchiha)
print(20 in uchiha) # in akan mengecek keberadaan keys, bukan values

''' Set 
    Set dibuat dengan tanda kurung kurawal ({}) di dalam set tidak ada elemen yang kembar, 
    tidak ada indeks (tidak dapat diakses berdasarkan posisinya),
    dan urutan data dalam set tidak penting
'''
my_set = {"Bokuto", "Bakugo", "Armin"}
print(my_set) # Perhatikan bahwa setiap kali di print maka urutannya berubah-ubah
print(type(my_set))

# Set dapat diperoleh dari list
list_saya = [21, 12, 121, 121]
m = set(list_saya)
print(m) 
# Perhatikan bahwa pada list yang di konversi ke set, maka urutan set tidak berubah
# Perhatikan juga bahwa elemen kembar hanya ditampilkan sebagai objek tunggal

## Menambahkan Elemen pada Set dengan Method add()
my_set = {"Bokuto", "Bakugo", "Armin"}
my_set.add("Midoriya") # Elemen Midoriya ditambahkan di posisi acak
print(my_set)

## Mengetahui Jumlah Elemen pada Set
my_set = {"Bokuto", "Bakugo", "Armin"}
print(len(my_set))

## Menghapus Elemen di Set dengan Method discard()
new_set = {"Todoroki", "Luffy", "Zoro"}
new_set.discard("Zoro") #  Case sensitive
print(new_set)

## Menghapus Elemen di Set dengan Method remove()
# Method remove() akan mengembalikkan eksepsi jika elemen yang ingin dihapus tidak ada di dalam set
new_set = {"Todoroki", "Luffy", "Zoro"}
new_set.remove("Zoro")
# new_set.remove("zoro") # Mengembalikkan eksepsi
print(new_set)

## Menghapus Seluruh Elemen di Set dengan Method clear()
new_set = {"Todoroki", "Luffy", "Zoro"}
new_set.clear()
print(new_set) # Set kosong

## Subset
# Adalah suatu set yang keseluruhan anggotanya ada di set lain
epsilon = {"Marksman", "Fighter", "Assasin"} # Subset dari gamma
gamma = {"Fighter", "Mage", "Tank", "Marksman", "Support", "Assasin"}
tetha = {"Goblin", "Marksman", "Fighter", "Assasin"} 

print(epsilon.issubset(gamma)) 
print(tetha.issubset(gamma)) 

## Superset
# Suatu set gamma adalah superset dari set epsilon jika set epsilon adalah subset dari set gamma
epsilon = {"Marksman", "Fighter", "Assasin"} # Subset dari gamma
gamma = {"Fighter", "Mage", "Tank", "Marksman", "Support", "Assasin"} # Superset dari epsilon
print(gamma.issuperset(epsilon))


## Union, Intersection, difference
# Format set_1.union(set_2) -> gabungan set
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
print(set1.union(set2))
print(set1 | set2) # Method union() bisa diganti dengan operator |

# Format  set_1.intersection(set_2) -> irisan set
setA = {2, 4, 6, 8, 10, 12}
setB = {1, 2, 3, 4, 5, 6}
print(setA.intersection(setB)) 
print(setA & setB) # Method intersection() bisa diganti dengan operator &

# Format set_1.difference(set_2) -> selisih elemen
set_1 = {1, 2, 3}
set_2 = {2, 4, 6}
print(set_1.difference(set_2)) 
print(set_1 - set_2) # Method difference() bisa diganti dengan operator -

print(set_2.difference(set_1))
print(set_2 - set_1) # Method difference() bisa diganti dengan operator -

print(set_1.symmetric_difference(set_2)) 
# Method tersebut untuk mendapatkan hasil gabungan dari kedua set yang dikurangi elemen-elemen yang sama pada kedua set
print(set_1 ^ set_2) # Dapat ditulis dengan operator ^

## Menentukan Keberadaan Suatu Elemen di dalam Set dengan in
sett = {"Delta", "Nu", "Zeta"}
print("zeta" in sett) # Case sensitive

## Menentukan Kesamaan Seluruh Elemen dari 2 Set dengan == dan !=
settA = {"Delta", "Nu", "Zeta"}
settB = {"Delta", "Beta", "Zeta"}
print(settA != settB)

## Menentukan Suatu Set sebagai Subset atau Superset dengan Operator Pembanding
a = {1, 3, 5}
b = {1, 2, 3, 4, 5, 6}
print(a < b) # Jika ini True berarti a merupakan subset dari b
print(a <= b) # Jika ini True berarti a merupakan subset dari b
print(a > b) # Jika ini True berarti a merupakan superset dari b
print(a >= b) # Jika ini True berarti a merupakan superset dari b
# Syarat subset adalah ketika set a anggotanya sama dengan set b dan set a maksimal memiliki jumlah anggota yang sama dengan b
# Syarat superset adalah ketika set a anggotanya sama dengan set b dan set a minimal memiliki jumlah anggota yang sama dengan b

''' String
    Method string cukup banyak seperti capitalize(), isalnum(), islowe() dll... (ada di w3school atau buku)
'''

''' Kloning
    Suatu variabel yang ditugaskan menyimpan sebuah values akan memiliki alamat yang sama
    jika diberikan penugasan seperti b = a. 
    Pada list cara b = a akan mempengaruhi isi dari list a dan b walaupun hanya salah satunya yang diubah
    dengan cara kloning hal ini dapat dihindari
'''
a = [1,2,3]
b = a # Memiliki 1 alamat
print(a)
print(b)

del a[-1]

print(a)
print(b)


a = [2, 4, 6]
b = a[:] # Kloning
print(a)
print(b)

del a[-1]
print(a)
print(b)


''' Latihan
    Latihan soal list,tuple, dan dictionary
'''

x = [1,2,3,4]
print(x[:-1])


## String dan Tuple bersifat immutable
z ="123"
# z[1] = "5" # Data bertipe string tidak bisa diubah
z = z[:1] + "5" + z[2:] # Cara ini dapat diterapkan untuk data bertipe string agar datanya dapat diubah
print(z)

y = (1,2,3)
# y[1] = 5 # Data tuple tidak bisa diubah
y = list(y) # Cara ini dapat diterapkan untuk data bertipe tuple agar datanya dapat diubah
y[1] = 5
y = tuple(y)
print(y)

## List bersifat mutable
x = [1,2,3]
x[1] = 5
print(x)

## Menampilkan elemen terbesar dari sebuah list
floch = [2, 5, 7, 2, 4, 1, 6, 2, 3]
print(max(floch))

## Menampilkan frekuensi elemen dari sebuah list
# Frekuensi elemen 2
floch = [2, 5, 7, 2, 4, 1, 6, 2, 3]
print(floch.count(2))

## Menampilkan nilai rata-rata dari sebuah list
floch = [2, 5, 7, 2, 4, 1, 6, 2, 3]
print(sum(floch)/len(floch))

## 
alter = set()
for i in range(0,8):
    alter.add(i * i)

print(alter)

## Menampilkan seluruh keys pada sebuah dictionary
all_keys = {"k": 1, "m": 2, "a": 3}
print(all_keys.keys())

## Menampilkan seluruh pasangan keys dan values pada sebuah dictionary
all_items = {"k": 1, "m": 2, "a": 3}
print(all_items.items())

## Menampilkan values dari suatu keys pada sebuah dictionary
k_value = {"k": 1, "m": 2, "a": 3}
print(k_value.get("k"))
print(k_value.setdefault("k"))


## Menghitung frekuensi karakter
kalimat = input("Masukkan suatu kalimat :")
jumlah_karakter = {}
for char in kalimat:
    # print(char)
    jumlah_karakter[char] = jumlah_karakter.get(char, 0) + 1 
    # Char (keys) yang belum ada akan disimpan dengan values 0 atau diwakili char jika char sudah ada

for char in jumlah_karakter.keys():
    if char == " ":
        print("Spasi = ", end=" ")
    else:
        print(char, "=", end=" ")
    print(jumlah_karakter[char])

