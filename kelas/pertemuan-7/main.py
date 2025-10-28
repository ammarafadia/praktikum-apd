# def perkenalan():
#     print('Halo, aku Nabil')

# perkenalan()

# def kali():
#     x = 5 * 5
#     print(x)

# kali()

# def perkenalan(nama):
#     print(f'Halo, aku {nama}')

# nama = 'Ridho'
# perkenalan(nama)

# def luaspersegipanjang (p, l):
#     luas = p * l
#     print(luas)

# def luaspersegipanjang (p, l):
#     luas = p * l
#     return luas

# print(luaspersegipanjang(4, 5))
# print(luaspersegipanjang(lebar=6, panjang=5))

# def segitiga (a, t):
#     luas = 0.5 * a * t
#     return luas

# print(segitiga(4, 4))

# def faktorial(n):
#     if n==1 or n==0:
#         return 1
#     else :
#         return n * faktorial(n-1)
    
# print(faktorial(5))

# film = []


# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#         for indeks in range(len(film)):
#             print(indeks+1, "|", film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")


# # Fungsi untuk mengedit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")


# # Fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")


# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# if __name__ == "__main__":
#         while (True):
#             show_menu()

nama = input("Masukkan nama: ")

if nama == "" or nama == " ":
    print("Nama tidak boleh kosong")
else:
    print("Nama anda", nama)