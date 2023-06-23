from __future__ import annotations
from src.FileHandler import *
from src.MemoryBuffer import MemoryBuffer
from src.Text import Text
from src.Statuses import Statuses
from src.Cipher_type import CipherType

class Menu:

    @staticmethod
    def display_menu(memory_buffer_len: int) -> None:
        if memory_buffer_len == 0:
            print("\n1. Dodaj napis do szyfrowania\n2. Dodaj napis do odszyfrowania\n3. Zamknij program")
        else:
            print(
                "\n1. Dodaj napis do szyfrowania\n2. Dodaj napis do odszyfrowania\n3. Zapisz wprowadzone napisy\n4. Wyświetl zawartość buffera\n5. Zamknij program")

    @classmethod
    def show_main_menu(cls, memory_buffer):
        Menu.display_menu(memory_buffer.get_length())
        option = input("Wybierz opcję: ")
        match option:
            case "1":
                cls.set_str_to_memory_buffer(memory_buffer, Statuses.TO_ENCRYPT.value)
            case "2":
                cls.set_str_to_memory_buffer(memory_buffer, Statuses.TO_DECRYPT.value)
            case "3":
                if memory_buffer.get_length() == 0:
                    print("Zamykam program")
                    exit()
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
                    exit()
            case _:
                print("Podano nieprawidłową opcję")

    @staticmethod
    def source_input():
        suboption = input("W jaki sposób chcesz podać dane:\n1.Wpisując ręcznie\n2.Wczytując tekst")
        return suboption

    @classmethod
    def set_str_to_memory_buffer(cls, memory_buffer: MemoryBuffer, *args: str) -> None:
        suboption = cls.source_input()
        match suboption:
            case '1':
                text = input("Podaj napis do zaszyfrowania: ")
                rot_type = cls.chose_rot_type()
                text_obj = Text(text, rot_type, args[0])
                memory_buffer.add_to_memory_buffer(text_obj)
            case '2':
                print("""Wczytany plik powinien mieć rozszerzenie .json i posiadać następującą strukturę
                [{"txt": "test do odszyfrowania/zaszyfrowania"}]""")
                file_name = input("Podaj nazwę pliku: ") + '.json'
                if FileHandler.check_file(file_name):
                    data = FileHandler.open(file_name)
                    rot_type = cls.chose_rot_type()
                    text_obj = Text(data, rot_type, args[0])
                    memory_buffer.add_to_memory_buffer(text_obj)
                else:
                    print("Podany plik nie istnieje")
                    cls.set_str_to_memory_buffer(memory_buffer, args[0])

    @classmethod
    def chose_rot_type(cls) -> str:
        print("\nDostępne rodzaje szyfrowań")
        CipherType.show_all()
        encrypt_option_chosen = int(input("Wybierz rodzaj szyfrowania: "))
        if list(CipherType)[encrypt_option_chosen - 1]:
            return list(CipherType)[encrypt_option_chosen - 1].value
        else:
            print("Podano nieprawidłową wartość!")
            cls.chose_rot_type()

    @classmethod
    def get_file_name(cls) -> tuple[str, (str, None)]:
        did_add_to_file = None
        file_name = input("Podaj nazwę pliku: ") + '.json'
        if os.path.isfile(file_name):
            did_add_to_file = input("Podana nazwa pliku istnieje. Czy chcesz dodać zawartość do pliku? [t/n]: ")
            if did_add_to_file == 't':
                did_add_to_file = 't'
            elif did_add_to_file == 'n':
                cls.get_file_name()
            else:
                print("Podano nieprawidłową akcję!")
                cls.get_file_name()
        return file_name, did_add_to_file

    @classmethod
    def save_to_file_question(cls, memory_buffer: MemoryBuffer, rot_tyoe: str, status: str):
        answer = input("Czy zapisać do pliku? [t/n]: ").lower()
        if isinstance(answer, str):
            if answer == 't':
                file_name, did_override = cls.get_file_name()
                if did_override == 't':
                    memory_buffer.insert_to_memory_buffer(0, FileHandler.append(file_name))
                for text in memory_buffer.memory_buffer:
                    file = Text(text, rot_tyoe, status)
                    FileHandler.save(file_name, did_override)
            elif answer == 'n':
                pass
            else:
                print("Podano nieprawidłowy znak")
                cls.save_to_file_question(memory_buffer)
        else:
            print("Podano nieprawidłowy znak")
            cls.save_to_file_question(memory_buffer)
