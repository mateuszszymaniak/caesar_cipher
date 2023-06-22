import os

from src.Cipher import *
from src.FileHandler import *
from src.MemoryBuffer import MemoryBuffer
from src.Text import Text

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

def save_to_file_question(memory_buffer: MemoryBuffer, rot_tyoe: str, status: str):
    answer = input("Czy zapisać do pliku? [t/n]: ").lower()
    if isinstance(answer, str):
        if answer == 't':
            file_name, did_override = get_file_name()
            if did_override == 't':
                memory_buffer.insert(0, FileHandler.append(file_name))
            for text in memory_buffer.memory_buffer:
                file = Text(text, rot_tyoe, status)
                FileHandler.save(file_name, did_override)
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

def str_to_decode(memory_buffer: MemoryBuffer) -> MemoryBuffer:
    print("\nPusty napis kończy dodawanie napisów do szyfrowania")
    while True:
        txt = input("Podaj tekst do zaszyfrowania: ")
        if txt == '':
            break
        memory_buffer.add_to_memory_buffer(txt)
    return memory_buffer

def source_input():
    suboption = input("W jaki sposób chcesz podać dane:\n1.Wpisując ręcznie\n2.Wczytując tekst")
    return suboption

def set_str_to_memory_buffer(memory_buffer: MemoryBuffer, *args: str) -> None:
    suboption = source_input()
    match suboption:
        case '1':
            text = input("Podaj napis do zaszyfrowania: ")
            rot_type = chose_rot_type()
            text_obj = Text(text, rot_type, args[0])
            memory_buffer.add_to_memory_buffer(text_obj)
        case '2':
            print("""Wczytany plik powinien mieć rozszerzenie .json i posiadać następującą strukturę
            [{"txt": "test do odszyfrowania/zaszyfrowania"}]""")
            file_name = input("Podaj nazwę pliku: ") + '.json'
            if FileHandler.check_file(file_name):
                data = FileHandler.open(file_name)
                rot_type = chose_rot_type()
                text_obj = Text(data, rot_type, args[0])
                memory_buffer.add_to_memory_buffer(text_obj)
            else:
                print("Podany plik nie istnieje")
                set_str_to_memory_buffer(memory_buffer, args[0])
def display_menu(memory_buffer_len: int) -> None:
    if memory_buffer_len == 0:
        print("\n1. Dodaj napis do szyfrowania\n2. Dodaj napis do odszyfrowania\n3. Zamknij program")
    else:
        print("\n1. Dodaj napis do szyfrowania\n2. Dodaj napis do odszyfrowania\n3. Zapisz wprowadzone napisy\n4. Wyświetl zawartość buffera\n5. Zamknij program")

def main():
    memory_buffer = MemoryBuffer
    print("Szyfr Cezara (ROT13/ROT47)")

    while True:
        display_menu(memory_buffer.get_length())
        option = input("Wybierz opcję: ")
        match option:
            case "1":
                set_str_to_memory_buffer(memory_buffer, "encrypted")
            case "2":
                set_str_to_memory_buffer(memory_buffer, "decrypted")
            case "3":
                if memory_buffer.get_length() == 0:
                    print("Zamykam program")
                    break
                else:
                    FileHandler.prepare_save(memory_buffer)
            case "4":
                if memory_buffer.get_length() == 0:
                    print("Podano nieprawidłową opcję")
                else:
                    memory_buffer.show_memory_buffer()
            case "5":
                if memory_buffer.get_length() == 0:
                    print("Podano nieprawidłową opcję")
                else:
                    print("Zamykam program")
                    break
            case _:
                print("Podano nieprawidłową opcję")


if __name__ == "__main__":
    main()
