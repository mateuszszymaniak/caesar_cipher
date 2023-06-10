def main():
    print("Szyfr Cezara (ROT13/ROT47)")
    print("1. Zaszyfruj tekst\n2. Odszyfruj tekst\n3. Wyjście z programu")

    while True:
        option = input("Wybierz opcję: ")
        match option:
            case "1":
                print("Szyfruję")
            case "2":
                print("Odszyfruję")
            case "3":
                print("Zamykam program")
                break
            case _:
                print("Podano nieprawidłową opcję")


if __name__ == "__main__":
    main()
