# num = int("42")
# name = str(123)
# data1 = list("abc")
# data = dict(a=1, b=2)
# print(type(num))
# print(type(data1))

# angka = 10
# print(bin(angka))

# buah = frozenset(["apel", "jeruk", "mangga"])
# print(buah)
# buahset = list(buah)

# angka = [1,2,3,4,5] ## absolut semua positif
# angka = 3.2456
# print(max(angka))
# print(min(angka))
# print(round(angka,2)) ## koma

# print(pow(2,5,2)) ## berapa pangkat modulus
# print(divmod(17,5)) ## hasil bagi dan sisa

# angka = [1,2,3,4,5,6]
# genap =  filter(lambda x: x%2==0, angka)
# ganjil =  filter(lambda x: x%2!=0, angka)
# print(list(genap))

# angka = [10,20,30]
# it = iter(angka)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) ##error

# nama = "daFFa anak jahat"
# print(nama.lower())
# print(nama.upper())
# print(nama.strip()) ## hapus spasi
# print(nama.replace("jahat", "baik")) ## mengubah

# huruf = "a,b,c"
# print(huruf.split(",")) ## memisahkan berdasarkan yang diminta
# print(nama.find("z"))

# import math 
# from math import sqrt
# import random

# print(math.sqrt(100))
# print(math.factorial(5))

# pilih_acak = ["pisang", "rambutan", "manggis"]
# print(random.choice(pilih_acak))

karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
kata_sandi = ""
pilih = int(input("pilihan"))
for i in range(1,pilih):
    
