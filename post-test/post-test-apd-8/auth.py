from utils import clear_screen, press_enter_to_continue

def check_credentials(users, username, password):
    return next((user for user in users if user["username"] == username and user["password"] == password), None)

def register(users):
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

def login(users):
    clear_screen()
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
    
    found_user = check_credentials(users, username, password)
    
    if found_user:
        print(f"Login berhasil! Selamat datang {username}")
        press_enter_to_continue()
        return found_user
    else:
        print("Error: Username atau password salah!")
        press_enter_to_continue()
        return None