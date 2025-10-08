#loop for
# for i in range(10):
#     print(i + 1)
# for i in range(1,11):
#     print(i)
# for i in range(1,11,2):
#     print(i)

# nama = ['bakil', 'diftya', 'anugrah']

# for i in nama:
#     print(i)

# for i in range(3):
#     print("Raffi")

#loop while
# jawab = "ya"
# hitung = 0

# while (jawab == "ya"):
#     hitung += 1
#     jawab = input("ulang lagi? : ")

# print(f"total jawab ya {hitung}")

# cuaca = "hujan"

# while (cuaca == "hujan" or cuaca == "Hujan"):
#     print("jangan keluar rumah")
#     cuaca = input("apa cuaca saat ini? ")

# print("pergi keluar rumah")

# angka = 10

# while(angka > 1):
#     print(angka)
#     angka -= 2

# for i in range(1,5):
#     for j in range(1,5):
#         print(f"{i} x {j} = {i * j}")
#     print()

# angka = [2, 5, 8, 12, 15, 7, 20]

# print("Mencari angka yang lebih besar dari 10....")

# for i in angka:
#     print(f"memeriksa angka {i}")
#     if i > 10:
#         print(f"{i} lebih besar dari 10")
#         break
    
# print("Program selesai")

# for i in range (1,11):
#     if i % 2 != 0:
#         continue
#     print(f"angka genap ditemukan yaitu {i}")

# print("program selesai")

# for i in range (1,11):
#     if i % 2 == 0:
#         continue
#     print(f"angka ditemukan yaitu {i}")

# print("program selesai")

# kuadrat = [i**2 for i in range (1,6)]
# print(kuadrat)

# for i in range(1,6):
#     print(i**2)

# genap = [i for i in range (1,11) if i % 2 == 0 ]
# print(genap)

# ganjil = [i for i in range (1,11) if i % 2 != 0 ]
# print(ganjil)

for i in range(1,6):
    print("*" * i)

print (" ")

for i in range(1,6):
    print("*" * (6 - i))