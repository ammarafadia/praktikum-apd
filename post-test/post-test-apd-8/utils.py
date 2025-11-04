import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter_to_continue():
    input("\nTekan Enter untuk melanjutkan...")

def view_all_users(users, PrettyTable):
    clear_screen()
    print("=== DAFTAR USER ===")
    if not users:
        print("Belum ada user terdaftar.")
    else:
        table = PrettyTable()
        table.field_names = ["No.", "Username", "Role"]
        table.align["Username"] = "l"
        table.align["Role"] = "c"

        for i, user in enumerate(users, 1):
            table.add_row([i, user['username'], user['role']])
        
        print(table)
    press_enter_to_continue()