from prettytable import PrettyTable
from utils import clear_screen, press_enter_to_continue

def is_title_unique(movies, title):
    return not any(film["judul"].lower() == title.lower() for film in movies)

def add_movie(movies, current_user):
    clear_screen()
    print("=== TAMBAH FILM/SERIES ===")
    judul = input("Judul film/series: ")
    genre = input("Genre: ")
    tahun = input("Tahun rilis: ")
    rating = input("Rating (1-10): ")
    
    if not all([judul, genre, tahun, rating]):
        print("Error: Semuanya harus diisi!")
    elif not is_title_unique(movies, judul):
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

def view_movies(movies):
    clear_screen()
    print("=== DAFTAR FILM/SERIES ===")
    if not movies:
        print("Belum ada film/series dalam koleksi.")
    else:
        table = PrettyTable()
        table.field_names = ["No.", "Judul", "Genre", "Tahun", "Rating", "Ditambahkan Oleh"]
        table.align["Judul"] = "l"
        table.align["Genre"] = "l"
        table.align["Rating"] = "c"

        for i, film in enumerate(movies, 1):
            table.add_row([i, film['judul'], film['genre'], film['tahun'], film['rating'], film['added_by']])
        
        print(table)
    press_enter_to_continue()

def edit_movie(movies, current_user):
    clear_screen()
    print("=== EDIT FILM/SERIES ===")

    if not movies:
        print("Belum ada film/series dalam koleksi.")
        press_enter_to_continue()
        return

    if current_user["role"] != "admin":
        print("Error: Hanya admin yang dapat mengedit film/series!")
        press_enter_to_continue()
        return

    table = PrettyTable()
    table.field_names = ["No.", "Judul", "Genre", "Tahun", "Rating"]
    for i, film in enumerate(movies, 1):
        table.add_row([i, film['judul'], film['genre'], film['tahun'], film['rating']])
    print(table)
    
    nomor = input("Pilih nomor film/series yang akan diedit: ")
    if nomor.isdigit():
        index = int(nomor) - 1
        if 0 <= index < len(movies):
            film = movies[index]
            print(f"\nEdit film: {film['judul']}")
            
            # Update Judul
            judul_baru = input(f"Judul baru ({film['judul']}): ")
            if judul_baru:
                film['judul'] = judul_baru

            # Update Genre
            genre_baru = input(f"Genre baru ({film['genre']}): ")
            if genre_baru:
                film['genre'] = genre_baru

            # Update Tahun
            tahun_baru = input(f"Tahun baru ({film['tahun']}): ")
            if tahun_baru:
                film['tahun'] = tahun_baru

            # Update Rating
            rating_baru = input(f"Rating baru ({film['rating']}): ")
            if rating_baru:
                if rating_baru.isdigit() and (1 <= int(rating_baru) <= 10):
                    film['rating'] = rating_baru
                    print("Film/Series berhasil diupdate!")
                else:
                    print("Error: Rating harus angka antara 1-10! Rating tidak diubah.")
            else:
                 print("Film/Series berhasil diupdate!")
        else:
            print("Error: Nomor film/series tidak valid!")
    else:
        print("Error: Input harus angka!")
        
    press_enter_to_continue()


def delete_movie(movies, current_user):
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

    table = PrettyTable()
    table.field_names = ["No.", "Judul", "Genre", "Tahun", "Rating"]
    for i, film in enumerate(movies, 1):
        table.add_row([i, film['judul'], film['genre'], film['tahun'], film['rating']])
    print(table)
    
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