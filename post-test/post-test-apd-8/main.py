from prettytable import PrettyTable
from auth import login, register
from movie_manager import add_movie, view_movies, edit_movie, delete_movie
from utils import clear_screen, press_enter_to_continue, view_all_users

users = [
    {"username": "admin", "password": "akuadminkausiapa", "role": "admin"},
]
movies = []
current_user = None

def main_menu_logged_in():
    global current_user, movies, users
    
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
            add_movie(movies, current_user)
        elif menu == "2":
            view_movies(movies)
        elif menu == "3":
            edit_movie(movies, current_user)
        elif menu == "4":
            delete_movie(movies, current_user)
        elif menu == "5" and current_user["role"] == "admin":
            view_all_users(users, PrettyTable) # Meneruskan users dan PrettyTable
        elif menu == "6":
            current_user = None
            print("Logout berhasil!")
            press_enter_to_continue()
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

def main_menu():
    global current_user, users
    
    while True:
        clear_screen()
        print("=== SISTEM MANAJEMEN FILM/SERIES ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            logged_in_user = login(users)
            if logged_in_user:
                current_user = logged_in_user
                main_menu_logged_in()
        elif pilihan == "2":
            register(users)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem!")
            break
        else:
            print("Pilihan tidak valid!")
            press_enter_to_continue()

if __name__ == "__main__":
    main_menu()