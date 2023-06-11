def rot13(txt: str) -> str:
    result = ""
    for letter in txt:
        if 65 <= ord(letter) <= 77 or 97 <= ord(letter) <= 109:
            result += chr(ord(letter) + 13)
        elif 78 <= ord(letter) <= 90 or 110 <= ord(letter) <= 122:
            result += chr(ord(letter) - 13)
        else:
            result += letter
    return result


def rot47(txt: str) -> str:
    result = ""
    for letter in txt:
        if 33 <= ord(letter) <= 81:
            result += chr(ord(letter) + 47)
        elif 82 <= ord(letter) <= 126:
            result += chr(ord(letter) - 47)
        else:
            result += letter
    return result

def encrypt(memory_buffer: list[str], encrypt_option: str) -> list[str]:
    encrypt_result = []
    for text in memory_buffer:
        if encrypt_option == 'ROT13':
            encrypt_result.append(rot13(text))
        elif encrypt_option == "ROT47":
            encrypt_result.append(rot47(text))
    return encrypt_result

def to_decode(memory_buffer: list[str]) -> list[str]:
    encrypt_options = ['ROT13', 'ROT47']
    print("\nPusty napis kończy dodawanie napisów do szyfrowania")
    while True:
        txt = input("Podaj tekst do zaszyfrowania: ")
        if txt == '':
            break
        memory_buffer.append(txt)
    print("\nDostępne rodzaje szyfrowań")
    for value, key in enumerate(encrypt_options, start=1):
        print(f"{value}. {key}")
    encrypt_option_chosen = int(input("Wybierz rodzaj szyfrowania: "))
    memory_buffer = encrypt(memory_buffer, encrypt_options[encrypt_option_chosen - 1])

    return memory_buffer

def main():
    memory_buffer = []
    print("Szyfr Cezara (ROT13/ROT47)")

    while True:
        print("\n1. Zaszyfruj tekst\n2. Odszyfruj tekst\n3. Wyjście z programu")
        option = input("Wybierz opcję: ")
        match option:
            case "1":
                to_decode(memory_buffer)
                print("Szyfruję")
            case "2":
                to_decode(memory_buffer)
                print("Odszyfruję")
            case "3":
                print("Zamykam program")
                break
            case _:
                print("Podano nieprawidłową opcję")


if __name__ == "__main__":
    main()
