# --- HEADER A ---
 feature/header-design-b
print('Witaj świecie')
def uruchom_menu():
    print("=== NOWE MENU ===")
    print("1. Start")
    print("2. O nas")
    print("3. Kontakt")
    print("4. Kalkulator")

if __name__ == '__main__':
    uruchom_menu()

import kalkulator

if wybor == "4":
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    print("Wynik dodawania:", kalkulator.dodaj(a, b))
