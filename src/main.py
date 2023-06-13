import os

from src.Cipher import *
from src.FileHandler import *

def chose_rot_type() -> str:
    encrypt_options = ['ROT13', 'ROT47']
    print("\nDostępne rodzaje szyfrowań")
    for value, key in enumerate(encrypt_options, start=1):
        print(f"{value}. {key}")
    encrypt_option_chosen = int(input("Wybierz rodzaj szyfrowania: "))
    if encrypt_option_chosen - 1 < len(encrypt_options):
        return encrypt_options[encrypt_option_chosen - 1]
    else:
        print("Podano nieprawidłową wartość!")
        chose_rot_type()

def get_file_name() -> tuple[str, (str, None)]:
    did_add_to_file = None
    file_name = input("Podaj nazwę pliku: ") + '.json'
    if os.path.isfile(file_name):
        did_add_to_file = input("Podana nazwa pliku istnieje. Czy chcesz dodać zawartość do pliku? [t/n]: ")
        if did_add_to_file == 't':
            did_add_to_file = 't'
        elif did_add_to_file == 'n':
            get_file_name()
        else:
            print("Podano nieprawidłową akcję!")
            get_file_name()
    return file_name, did_add_to_file

def save_to_file_question(memory_buffer: list[str], rot_tyoe: str, status: str):
    answer = input("Czy zapisać do pliku? [t/n]: ").lower()
    if isinstance(answer, str):
        if answer == 't':
            file_name, did_override = get_file_name()
            if did_override == 't':
                memory_buffer.insert(0, FileHandler.append(file_name))
            for text in memory_buffer:
                file = FileHandler(text, rot_tyoe, status)
                file.save(file_name, did_override)
        elif answer == 'n':
            pass
        else:
            print("Podano nieprawidłowy znak")
            save_to_file_question(memory_buffer)
    else:
        print("Podano nieprawidłowy znak")
        save_to_file_question(memory_buffer)


def encrypt(memory_buffer: list[str], encrypt_option: str) -> list[str]:
    encrypt_result = []
    for text in memory_buffer:
        if encrypt_option == 'ROT13':
            encrypt_result.append(Cipher.rot13(text))
        elif encrypt_option == "ROT47":
            encrypt_result.append(Cipher.rot47(text))
    return encrypt_result

def str_to_decode(memory_buffer: list[str]) -> list[str]:
    print("\nPusty napis kończy dodawanie napisów do szyfrowania")
    while True:
        txt = input("Podaj tekst do zaszyfrowania: ")
        if txt == '':
            break
        memory_buffer.append(txt)
    return memory_buffer

def main():
    memory_buffer = []
    print("Szyfr Cezara (ROT13/ROT47)")

    while True:
        print("\n1. Zaszyfruj tekst\n2. Odszyfruj tekst\n3. Wyjście z programu")
        option = input("Wybierz opcję: ")
        match option:
            case "1":
                str_to_decode(memory_buffer)
                rot_type = chose_rot_type()
                memory_buffer = encrypt(memory_buffer, rot_type)
                save_to_file_question(memory_buffer, rot_type, "encrypted")
            case "2":
                str_to_decode(memory_buffer)
            case "3":
                print("Zamykam program")
                break
            case _:
                print("Podano nieprawidłową opcję")


if __name__ == "__main__":
    main()
