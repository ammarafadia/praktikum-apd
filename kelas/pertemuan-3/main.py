# angka = 5

# if angka > 5:
#     print("angka lebih besar 5")
# # tidak keluar output karena 5 tidak lebih besar dari 5

# cuaca = "hujan"

# if cuaca == "hujan":
#     print("Di rumah aja")
# else :
#     print("Nongkrong")

# nilai = 70

#  if nilai >= 70:
#      print("lulus")
#  else:
#      print("tidak lulus")

# status = "Lulus" if nilai>= 70 else "Tidak Lulus"
# print(status)

# cuaca = 'mendung'

# if cuaca == "hujan":
#     print("dirumah aja")
# elif cuaca == "mendung":
#     print("makan mie")
# else :
#     print("nongkrong")

# usia = int(input("masukkan usia anda:"))

# if usia <= 13:
#     print("anak-anak")
# elif usia <= 18:
#     print("remaja")
# elif usia <= 40:
#     print("dewasa")
# else :
#     print("lansia")

# nilai = int(input("masukkan nilai anda:"))

# if nilai >= 90:
#     print("A")
# elif nilai >= 70:
#     print("B")
# elif nilai >= 60:
#     print("C")
# else :
#     print("D")

# a = 2
# b = 5
# c = 6

# if a<b :
#     if a<c:
#         print("a paling kecil")
#     else :
#        print("c lebih kecil dari a")
# elif a<c:
#    print("c lebih besar")
# else:
#     print("a paling besar")

# tinggi_badan = float(input("Masukkan tinggi:"))

# if tinggi_badan >= 145:
#     print("cihuy bisa naik wahana")
# else:
#     print("nda bole naik, wlee")

# a = 100000
# b = 50000

# harga = int(input("harga:"))

# if harga > a:
#     print("anda mendapatkan diskon 20%")
#     hasil1 = harga * 0.2
#     print(hasil1)
# elif harga > b:
#     print("anda mendapatkan diskon 10%")
#     hasil2 = harga * 0.1
#     print(hasil2)
# else:
#     print("anda tidak mendapatkan diskon")

nilai = int(input("Masukkan nilai:"))
kelas = input("Masukkan kelas:")

if nilai >= 80 and kelas == "A": #or kelas == "a"
    print("IPK 4")
elif nilai >= 80 and kelas == "B":
    print("IPK 3")
else :
    print("IPK 2")