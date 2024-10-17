from logowanie import Auth
from roles import Role
from uzytkownik import MenagerUzytkownika

def admin_menu(user_menager):
    print("Witaj administratoze!")
    print("==="*10)
    print("Znajdujesz sie w miejscu gdzie mozesz zmienic dane uzytkownikow !")
    while True:
        print("==="*10)
        print("a - zmien role uzytkownika")
        print("b - edytuj chaslo")
        print("e - wyjdz")
        print("==="*10)
        inp = str(input("Wybiez opcje: "))
        print(inp)

        if inp == "a":
            username = input("Podaj nazwe uzytkownika, ktorego role chcesz zmienic: ")
            new_role = input("Podaj nowa role(Sigma, Informatyka, User): ")
            if new_role in [Role.Admin, Role.Sprzedawca, Role.Uzytkownik]:
                try:
                    user_menager.update_user_role(username, new_role)
                    print(f"Zmieniono rolę użytkownika {username} na {new_role}.")
                except ValueError as e:
                    print(e)
            else:
                print("Nieprawidłowa rola.")
            
        elif inp == "e":
            break
        else:
            print("Nieprawidlowa komenda")


def main():
    user_manager = MenagerUzytkownika()

    try:
        user_manager.add_user("admin", Role.Admin, "xd123")
        user_manager.add_user("sprzedawca", Role.Sprzedawca, "xd321")
        user_manager.add_user("uzytkownik", Role.Uzytkownik, "xdxd")
    except ValueError as e:
        print(e)

    auth = Auth(user_manager)

    zalogowany = False

    while not zalogowany:
        try:
            username = input("Podaj nazwę użytkownika (Sigma, Informatyka, User) (lub wpisz 'exit', aby zakończyć): ")
            password = input("Podaj chaslo:")
            if username.lower() == 'exit':
                print("Zakończono logowanie.")
                break

            user = auth.login(username, password)
            zalogowany = True
            
            if user["role"] == Role.Admin:
                print("Jesteś administratorem.")
                print("==="*10)
                admin_menu(user_manager)
            else:
                print(f"Jesteś zalogowany jako {user['role']}.")
        
        except ValueError as e:
            print(e)
            print("Spróbuj ponownie.")

main()
