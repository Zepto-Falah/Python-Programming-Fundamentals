''' Memasukkan Data Dengan Input '''

data = list(input("Masukkan data:"))
data = tuple(input("Masukkan data:"))
data = int(input("Masukkan data:"))
data = float(input("Masukkan data:"))

print(data)

print("Menjumlahkan dua bilangan.")
x = int(input("bilangan pertama: "))
y = int(input("bilangan kedua: "))

print("Jumlah = ", (x+y))
print(x, y)

''' Menampilkan Output dengan Print() '''

x = 22
y = 33
print("Dua nilai dalam baris berbeda")
print(x)
print(y)

print("Dua nilai dalam baris yang sama")
print("dengan pemisah berupa satu spasi")
print(x, end=" ") # end disini menggunakan satu spasi agar output terpisah satu spasi 
print(y)

print("dengan pemisah tanpa spasi")
print(x, end="") # end disini tidak menggunakan satu spasi agar output tidak terpisah satu spasi 
print(y)

print("dengan pemisah berupa *")
print(x, end="*") # end disini  menggunakan * agar output dipisahkan oleh *
print(y)

print("Messi", "Ronaldo", "Neymar", sep=" Vs ")
print("Messi", "Ronaldo", "Neymar", sep="-") # sep berguna untuk menentukan jenis pemisah antarnilai
# Jika tidak ada penentuan sep, pemisah yang digunakan antarnilai adalah spasi


''' Menampilkan Sejumlah String dengan Operator + '''
print("Lionel Messi " +\
    "telah memenangkan " +\
    "Piala Dunia 2022 di Qatar ")


''' Memformat Output Print() '''
hewan = "Kucing"
print("Saya memelihara seekor %s" % hewan) # Operator % disebut operator format
''' %c untuk karakter
    %s untuk string
    %d untuk bilangan bulat
    %i untuk bilangan bulat
    %o untuk bilangan oktal
    %x untuk bilangan heksadesimal (huruf kecil)
    %X untuk bilangan heksadesimal (huruf kapital)
    %e untuk float dengan bentuk m.dddddde+-xx
    %E untuk float dengan bentuk m.ddddddE+-xx
    %f untuk float dengan bentuk m.dddddd
    %g, %G untuk float dengan bentuk eksponen
    %% untuk karakter %'''

#Example
p = -254
q = 2.4678e-4 

print("Format %%i : %i" % p)
print("Format %%d : %d" % p)
print("Format %%o : %o" % p)
print("Format %%x : %x" % p)
print("Format %%X : %X" % p)
print("Format %%s : %s" % p)

print("Format %%e : %e" % q)
print("Format %%E : %E" % q)
print("Format %%f : %f" % q)
print("Format %%g : %g" % q)
print("Format %%G : %G" % q)
print("Format %%s : %s" % q)

# Mengatur lebar format
a = 133
print("%d" % a)
print("%6d" % a) # berjarak 6 dari kiri termasuk digit angka
print("%8d" % a)
print("%-8d" % a) # berjarak 8 dari kanan termasuk digit angka (rata kanan)
print("%+d" % 189) 
print("%+d" % -189) # tanda + membuat nilai ditampilkan dengan tanda positif(+) atau negatif(-)

# format 0.n
# dengan n sebgai pengatur berbagai hal tergantung kode formatnya
print("%0.4f" % 3.14) # n = 4 pada kode format ini, untuk menentukan jumlah digit pecahan sebanyak 4 angka
print("%0.4d" % 97) # n = 4 pada kode format ini, untuk menentukan penambah 0 dibagian awal bilangan agar menjadi 4 digit
print("%0.4s" % "zepto") # n = 4 pada kode format ini, untuk menentukan jumlah karakter yang ditampilkan


''' Pemformatan Bilangan dengan Format() '''
## Pemformatan Bilangan Bulat
format(113, "o") # format(bilangan, "string pemformat")
print(format(113,"o")) # 113 jika ingin diformat ke oktal
print(format(113,"b")) # diformat ke biner
print(format(113,"c")) # diformat ke character
print(format(113,"X")) # diformat ke bilangan heksadesimal

print(format(75, "#o")) 
print(format(75, "#b")) 
print(format(75, "#X")) 
# tanda # akan menampilkan 0o untuk bil.oktal, 0b untuk bil.biner, dan 0x untuk bil.heksadesimal

## Pemformatan Bilangan Float
print(format(1234.56789, ".4f")) # angka 4 pada .4f artinya bilangan akan dibulatkan menjadi 4 angka dibelakang koma
print(format(1234.56789, ".2f"))
print(format(1234.56789, ".0f")) # 0.5 akan dibulatkan ke atas

## Format Notasi Sains
print(format(987.654321, "e"))
print(format(987.654321, "E"))
print(format(987.654321, ".3E")) # angka 3 pada .3E berfungsi untuk mengatur jumlah digit setelah koma

## Pemformatan Lebar Medan Output
print(format(1234.56789, ".2f")) 
print(format(1234.56789, "8.2f")) 
print(format(1234.56789, "10.2f")) # angka 10 pada 10.2f berfungsi untuk memformat lebar medan output

## Pemformatan Posisi Bilangan di dalam Medan yang Disediakan
print("1234567890|1234567890|1234567890")
# Pemformatan rata-kiri
print(format(345.12345, "<10.2f"),end= "|")
print(format(987.34567, "<10.2f"),end= "|")
print(format(567.32145, "<10.2f")) # simbol < berfungsi untuk membuat bilangan menjadi rata-kiri, tetapi angka 10 juga mempengaruhi
# Pemformatan di Tengah
print(format(345.12345, "^10.2f"),end= "|")
print(format(987.34567, "^10.2f"),end= "|")
print(format(567.32145, "^10.2f")) # simbol ^ berfungsi untuk membuat bilangan menjadi ditengah, tetapi angka 10 juga mempengaruhi
#Pemformatan rata-kanan
print(format(345.12345, ">10.2f"),end= "|")
print(format(987.34567, ">10.2f"),end= "|")
print(format(567.32145, ">10.2f")) # simbol > berfungsi untuk membuat bilangan menjadi rata-kanan, tetapi angka 10 juga mempengaruhi

## Penyajian Tanda + untuk Bilangan Positif
print(format(432,"+"))
print(format(-432,"+"))
print(format(432,"+5")) # angka 5 merupakan lebar medannya, yaitu 5 karakter

## Pemformatan Angka Pecahan dalam Bentuk Persen
print(format(.8, "%")) # dikembalikan dengan bentuk persen dan 6 angka dibelakang koma
print(format(0.8, "8.2%")) # angka 8 sebagai lebar medannya, yaitu 8 karakter dan angka 2 sebagai jumlah digit dibelakang koma

## Pemformatan Pemisah Ribuan
print(format(987654321.3456, ".2f")) 
print(format(987654321.3456, ",.2f")) # hanya tanda (,) sebagai format pemisah ribuan

# Latihan
print("%s", "Berlin") # menggunakan koma (,) akan memisahkan dengan spasi
print("%s" + "Berlin") # menggunakan + tidak akan dipisah dengan spasi
print("%s" % "Berlin") # memasukkan string Berlin ke placeholder format %s

print("%6d", 389)
print("%+6d", 389)
print("%-6d", 389)

print(format(123412.09401, "+10.2f"))

print("\nMenghitung Luas Lingkaran dan Memformat Menjadi Bilangan Bulat (dibulatkan)\n")
r = int(input("Masukkan panjang jari-jari lingkaran (cm): "))
luas_lingkaran = 3.14*(r**2)
print("Luas Lingkaran = " + format(luas_lingkaran, ".0f"), "cm^2")