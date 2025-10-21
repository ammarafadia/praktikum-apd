import os

# Menyimpan data
users = [
    {"username": "admin", "password": "akuadminkausiapa", "role": "admin"}
]

movies = []

current_user = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # clear

# Menu utama
while True:
    clear_screen()
    print("=== SISTEM MANAJEMEN FILM/SERIES ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1-3): ")
    
    if pilihan == "1":
        clear_screen()
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")
        
        # Cek login
        login_sukses = False
        for user in users:
            if user["username"] == username and user["password"] == password:
                current_user = user
                login_sukses = True
                break
        
        if login_sukses:
            print(f"Login berhasil! Selamat datang {username}")
            input("Tekan Enter untuk melanjutkan...")
            
            # Menu setelah login
            while True:
                clear_screen()
                print(f"=== MENU UTAMA ({current_user['username']}) ===")
                print("1. Tambah Film/Series")
                print("2. Lihat Semua Film/Series")
                print("3. Edit Film/Series")
                print("4. Hapus Film/Series")
                if current_user["role"] == "admin":
                    print("5. Lihat Semua User")
                print("6. Logout")
                
                menu = input("Pilih menu (1-6): ")
                
                if menu == "1":  # Tambah film/series
                    clear_screen()
                    print("=== TAMBAH FILM/SERIES ===")
                    judul = input("Judul film/series: ")
                    genre = input("Genre: ")
                    tahun = input("Tahun rilis: ")
                    rating = input("Rating (1-10): ")
                    
                    # Validasi input
                    if not judul or not genre or not tahun or not rating:
                        print("Error: Semuanya harus diisi!")
                    else:
                        # Cek apakah judul sudah ada
                        judul_ada = False
                        for film in movies:
                            if film["judul"].lower() == judul.lower():
                                judul_ada = True
                                break
                        
                        if judul_ada:
                            print("Error: Film/series dengan judul tersebut sudah ada!")
                        else:
                            # Validasi rating
                            if rating.isdigit():
                                rating_num = int(rating)
                                if 1 <= rating_num <= 10:
                                    film_baru = {
                                        "judul": judul,
                                        "genre": genre,
                                        "tahun": tahun,
                                        "rating": rating,
                                        "added_by": current_user["username"]
                                    }
                                    movies.append(film_baru)
                                    print("Film/Series berhasil ditambahkan!")
                                else:
                                    print("Error: Rating harus antara 1-10!")
                            else:
                                print("Error: Rating harus angka antara 1-10!")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif menu == "2":  # Lihat semua film/series
                    clear_screen()
                    print("=== DAFTAR FILM/SERIES ===")
                    if not movies:
                        print("Belum ada film/series dalam koleksi.")
                    else:
                        for i, film in enumerate(movies, 1):
                            print(f"{i}. {film['judul']} - {film['genre']} ({film['tahun']}) - Rating: {film['rating']} - Ditambahkan oleh: {film['added_by']}")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif menu == "3":  # Edit film/series
                    clear_screen()
                    print("=== EDIT FILM/SERIES ===")
                    if not movies:
                        print("Belum ada film/series dalam koleksi.")
                    else:
                        for i, film in enumerate(movies, 1):
                            print(f"{i}. {film['judul']} - {film['genre']} ({film['tahun']}) - Rating: {film['rating']}")
                        
                        nomor = input("Pilih nomor film/series yang akan diedit: ")
                        if nomor.isdigit():
                            index = int(nomor) - 1
                            if 0 <= index < len(movies):
                                film = movies[index]
                                # Cek akses - hanya admin yang bisa edit
                                if current_user["role"] == "admin":
                                    print(f"Edit film: {film['judul']}")
                                    judul_baru = input(f"Judul baru ({film['judul']}): ") or film['judul']
                                    genre_baru = input(f"Genre baru ({film['genre']}): ") or film['genre']
                                    tahun_baru = input(f"Tahun baru ({film['tahun']}): ") or film['tahun']
                                    rating_baru = input(f"Rating baru ({film['rating']}): ") or film['rating']
                                    
                                    # Validasi rating baru
                                    if rating_baru.isdigit():
                                        rating_num = int(rating_baru)
                                        if 1 <= rating_num <= 10:
                                            movies[index] = {
                                                "judul": judul_baru,
                                                "genre": genre_baru,
                                                "tahun": tahun_baru,
                                                "rating": rating_baru,
                                                "added_by": film['added_by']
                                            }
                                            print("Film/Series berhasil diupdate!")
                                        else:
                                            print("Error: Rating harus antara 1-10!")
                                    else:
                                        print("Error: Rating harus angka antara 1-10!")
                                else:
                                    print("Error: Hanya admin yang dapat mengedit film/series!")
                            else:
                                print("Error: Nomor film/series tidak valid!")
                        else:
                            print("Error: Input harus angka!")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif menu == "4":  # Hapus film/series
                    clear_screen()
                    print("=== HAPUS FILM/SERIES ===")
                    if not movies:
                        print("Belum ada film/series dalam koleksi.")
                    else:
                        for i, film in enumerate(movies, 1):
                            print(f"{i}. {film['judul']} - {film['genre']} ({film['tahun']}) - Rating: {film['rating']}")
                        
                        nomor = input("Pilih nomor film/series yang akan dihapus: ")
                        if nomor.isdigit():
                            index = int(nomor) - 1
                            if 0 <= index < len(movies):
                                film = movies[index]
                                # Cek hak akses - hanya admin yang bisa hapus
                                if current_user["role"] == "admin":
                                    konfirmasi = input(f"Yakin hapus film/series '{film['judul']}'? (yes/no): ")
                                    if konfirmasi.lower() == 'yes':
                                        movies.pop(index)
                                        print("Film/Series berhasil dihapus!")
                                else:
                                    print("Error: Hanya admin yang dapat menghapus film/series!")
                            else:
                                print("Error: Nomor film/series tidak valid!")
                        else:
                            print("Error: Input harus angka!")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif menu == "5" and current_user["role"] == "admin":  # Lihat semua user (admin only)
                    clear_screen()
                    print("=== DAFTAR USER ===")
                    for i, user in enumerate(users, 1):
                        print(f"{i}. {user['username']} - Role: {user['role']}")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif menu == "6":  # Logout
                    current_user = None
                    print("Logout berhasil!")
                    input("Tekan Enter untuk melanjutkan...")
                    break
                
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk melanjutkan...")
        
        else:
            print("Error: Username atau password salah!")
            input("Tekan Enter untuk melanjutkan...")
    
    elif pilihan == "2":
        clear_screen()
        print("=== REGISTER ===")
        username = input("Username: ")
        password = input("Password: ")
        
        # Cek apakah username sudah ada
        username_ada = False
        for user in users:
            if user["username"] == username:
                username_ada = True
                break
        
        if username_ada:
            print("Error: Username sudah digunakan!")
        elif username and password:
            user_baru = {
                "username": username,
                "password": password,
                "role": "user"
            }
            users.append(user_baru)
            print("Registrasi berhasil! silahkan login.")
        else:
            print("Error: Username dan password harus diisi!")
        input("Tekan Enter untuk melanjutkan...")
    
    elif pilihan == "3":
        print("Terima kasih telah menggunakan sistem!")
        break
    
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk melanjutkan...")