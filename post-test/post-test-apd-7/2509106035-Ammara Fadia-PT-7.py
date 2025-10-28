import os

users = [
    {"username": "admin", "password": "akuadminkausiapa", "role": "admin"}
]
movies = []
current_user = None

# Fungsi Utility
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter_to_continue():
    input("Tekan Enter untuk melanjutkan...")

def check_credentials(username, password):
    return next((user for user in users if user["username"] == username and user["password"] == password), None)

def is_title_unique(title):
    return not any(film["judul"].lower() == title.lower() for film in movies)

# Fungsi User/Auth
def register():
    global users
    clear_screen()
    print("=== REGISTER ===")
    username = input("Username: ")
    password = input("Password: ")
    
    if any(user["username"] == username for user in users):
        print("Error: Username sudah digunakan!")
    elif username and password:
        new_user = {
            "username": username,
            "password": password,
            "role": "user"
        }
        users.append(new_user)
        print("Registrasi berhasil! Silakan login.")
    else:
        print("Error: Username dan password harus diisi!")
    press_enter_to_continue()

def login():
    global current_user
    clear_screen()
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
    
    found_user = check_credentials(username, password)
    
    if found_user:
        current_user = found_user
        print(f"Login berhasil! Selamat datang {username}")
        press_enter_to_continue()
        main_menu_logged_in()
    else:
        print("Error: Username atau password salah!")
        press_enter_to_continue()

def view_all_users():
    clear_screen()
    print("=== DAFTAR USER ===")
    for i, user in enumerate(users, 1):
        print(f"{i}. {user['username']} - Role: {user['role']}")
    press_enter_to_continue()

# Fungsi Manajemen Film/Series
def add_movie():
    global movies
    clear_screen()
    print("=== TAMBAH FILM/SERIES ===")
    judul = input("Judul film/series: ")
    genre = input("Genre: ")
    tahun = input("Tahun rilis: ")
    rating = input("Rating (1-10): ")
    
    if not all([judul, genre, tahun, rating]):
        print("Error: Semuanya harus diisi!")
    elif not is_title_unique(judul):
        print("Error: Film/series dengan judul tersebut sudah ada!")
    elif not rating.isdigit() or not (1 <= int(rating) <= 10):
        print("Error: Rating harus angka antara 1-10!")
    else:
        new_movie = {
            "judul": judul,
            "genre": genre,
            "tahun": tahun,
            "rating": rating,
            "added_by": current_user["username"]
        }
        movies.append(new_movie)
        print("Film/Series berhasil ditambahkan!")
    press_enter_to_continue()

def view_movies():
    clear_screen()
    print("=== DAFTAR FILM/SERIES ===")
    if not movies:
        print("Belum ada film/series dalam koleksi.")
    else:
        for i, film in enumerate(movies, 1):
            print(f"{i}. {film['judul']} - {film['genre']} ({film['tahun']}) - Rating: {film['rating']} - Ditambahkan oleh: {film['added_by']}")
    press_enter_to_continue()

def edit_movie():
    global movies
    clear_screen()
    print("=== EDIT FILM/SERIES ===")

    def update_judul(film):
        film['judul'] = input(f"Judul baru ({film['judul']}): ") or film['judul']

    def update_genre(film):
        film['genre'] = input(f"Genre baru ({film['genre']}): ") or film['genre']
    
    def update_tahun(film):
        film['tahun'] = input(f"Tahun baru ({film['tahun']}): ") or film['tahun']

    def validate_and_update_rating(film):
        rating_baru = input(f"Rating baru ({film['rating']}): ") or film['rating']
        if rating_baru.isdigit() and (1 <= int(rating_baru) <= 10):
            film['rating'] = rating_baru
            return True
        else:
            print("Error: Rating harus angka antara 1-10! Rating tidak diubah.")
            return False

    def check_admin_access():
        if current_user["role"] != "admin":
            print("Error: Hanya admin yang dapat mengedit film/series!")
            press_enter_to_continue()
            return False
        return True

    if not movies:
        print("Belum ada film/series dalam koleksi.")
        press_enter_to_continue()
        return

    if not check_admin_access():
        return

    for i, film in enumerate(movies, 1):
        print(f"{i}. {film['judul']} - {film['genre']} ({film['tahun']}) - Rating: {film['rating']}")
    
    nomor = input("Pilih nomor film/series yang akan diedit: ")
    if nomor.isdigit():
        index = int(nomor) - 1
        if 0 <= index < len(movies):
            film = movies[index]
            print(f"\nEdit film: {film['judul']}")
            
            # Panggil Prosedur Lokal
            update_judul(film)
            update_genre(film)
            update_tahun(film)
            
            success = validate_and_update_rating(film)
            if success:
                 print("Film/Series berhasil diupdate!")

        else:
            print("Error: Nomor film/series tidak valid!")
    else:
        print("Error: Input harus angka!")
        
    press_enter_to_continue()

def delete_movie():
    global movies
    clear_screen()
    print("=== HAPUS FILM/SERIES ===")
    if not movies:
        print("Belum ada film/series dalam koleksi.")
        press_enter_to_continue()
        return

    if current_user["role"] != "admin":
        print("Error: Hanya admin yang dapat menghapus film/series!")
        press_enter_to_continue()
        return

    for i, film in enumerate(movies, 1):
        print(f"{i}. {film['judul']} - {film['genre']} ({film['tahun']}) - Rating: {film['rating']}")
    
    nomor = input("Pilih nomor film/series yang akan dihapus: ")
    if not nomor.isdigit():
        print("Error: Input harus angka!")
        press_enter_to_continue()
        return

    index = int(nomor) - 1
    if not (0 <= index < len(movies)):
        print("Error: Nomor film/series tidak valid!")
        press_enter_to_continue()
        return
    
    film_to_delete = movies[index]
    konfirmasi = input(f"Yakin hapus film/series '{film_to_delete['judul']}'? (yes/no): ")
    if konfirmasi.lower() == 'yes':
        movies.pop(index)
        print("Film/Series berhasil dihapus!")
    else:
        print("Batal menghapus.")
        
    press_enter_to_continue()

# Fungsi Menu
def main_menu_logged_in():
    global current_user
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
        
        menu = input("Pilih menu: ")
        
        if menu == "1":
            add_movie()
        elif menu == "2":
            view_movies()
        elif menu == "3":
            edit_movie()
        elif menu == "4":
            delete_movie()
        elif menu == "5" and current_user["role"] == "admin":
            view_all_users()
        elif menu == "6":
            current_user = None
            print("Logout berhasil!")
            press_enter_to_continue()
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def main_menu():
    while True:
        clear_screen()
        print("=== SISTEM MANAJEMEN FILM/SERIES ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            login()
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem!")
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

if __name__ == "__main__":
    main_menu()