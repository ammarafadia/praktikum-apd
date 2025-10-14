import os

# Menyimpan data
users = [["admin", "akuadminkausiapa", "admin"]]
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
            if user[0] == username and user[1] == password:
                current_user = user
                login_sukses = True
                break
        
        if login_sukses:
            print(f"Login berhasil! Selamat datang {username}")
            input("Tekan Enter untuk melanjutkan...")
            
            # Menu setelah login
            while True:
                clear_screen()
                print(f"=== MENU UTAMA ({current_user[0]}) ===")
                print("1. Tambah Film/Series")
                print("2. Lihat Semua Film/Series")
                print("3. Edit Film/Series")
                print("4. Hapus Film/Series")
                if current_user[2] == "admin":
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
                    
                    if judul and genre and tahun and rating:
                        film_baru = [judul, genre, tahun, rating, current_user[0]]
                        movies.append(film_baru)
                        print("Film/Series berhasil ditambahkan!")
                    else:
                        print("Error: Semuanya harus diisi!")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif menu == "2":  # Lihat semua film/series
                    clear_screen()
                    print("=== DAFTAR FILM/SERIES ===")
                    if not movies:
                        print("Belum ada film/series dalam koleksi.")
                    else:
                        for i, film in enumerate(movies, 1):
                            print(f"{i}. {film[0]} - {film[1]} ({film[2]}) - Rating: {film[3]} - Ditambahkan oleh: {film[4]}")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif menu == "3":  # Edit film/series
                    clear_screen()
                    print("=== EDIT FILM/SERIES ===")
                    if not movies:
                        print("Belum ada film/series dalam koleksi.")
                    else:
                        for i, film in enumerate(movies, 1):
                            print(f"{i}. {film[0]} - {film[1]} ({film[2]}) - Rating: {film[3]}")
                        
                        nomor = input("Pilih nomor film/series yang akan diedit: ")
                        if nomor.isdigit():
                            index = int(nomor) - 1
                            if 0 <= index < len(movies):
                                film = movies[index]
                                # Cek hak akses
                                if film[4] == current_user[0] or current_user[2] == "admin":
                                    print(f"Edit film: {film[0]}")
                                    judul_baru = input(f"Judul baru ({film[0]}): ") or film[0]
                                    genre_baru = input(f"Genre baru ({film[1]}): ") or film[1]
                                    tahun_baru = input(f"Tahun baru ({film[2]}): ") or film[2]
                                    rating_baru = input(f"Rating baru ({film[3]}): ") or film[3]
                                    
                                    movies[index] = [judul_baru, genre_baru, tahun_baru, rating_baru, film[4]]
                                    print("Film/Series berhasil diupdate!")
                                else:
                                    print("Error: Anda hanya bisa mengedit film/series yang Anda tambahkan!")
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
                            print(f"{i}. {film[0]} - {film[1]} ({film[2]}) - Rating: {film[3]}")
                        
                        nomor = input("Pilih nomor film/series yang akan dihapus: ")
                        if nomor.isdigit():
                            index = int(nomor) - 1
                            if 0 <= index < len(movies):
                                film = movies[index]
                                # Cek hak akses
                                if film[4] == current_user[0] or current_user[2] == "admin":
                                    konfirmasi = input(f"Yakin hapus film/series '{film[0]}'? (yes/no): ")
                                    if konfirmasi.lower() == 'yes':
                                        movies.pop(index)
                                        print("Film/Series berhasil dihapus!")
                                else:
                                    print("Error: Anda hanya bisa menghapus film/series yang Anda tambahkan!")
                            else:
                                print("Error: Nomor film/series tidak valid!")
                        else:
                            print("Error: Input harus angka!")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif menu == "5" and current_user[2] == "admin":  # Lihat semua user (admin only)
                    clear_screen()
                    print("=== DAFTAR USER ===")
                    for i, user in enumerate(users, 1):
                        print(f"{i}. {user[0]} - Role: {user[2]}")
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
            if user[0] == username:
                username_ada = True
                break
        
        if username_ada:
            print("Error: Username sudah digunakan!")
        elif username and password:
            user_baru = [username, password, "user"]
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