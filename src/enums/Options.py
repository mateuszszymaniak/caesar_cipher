from enum import Enum
from src.enums.Messages import Messages

class Options(Enum):
    ADD_STR_TO_ENCRYPT = "Dodaj napis do szyfrowania"
    ADD_STR_TO_DECRYPT = "Dodaj napis do odszyfrowania"
    SAVE_STR_TO_FILE = "Zapisz napisy do pliku"
    SHOW_STR = "Wyświetl napisy"
    EXIT = "Zamknięcie programu"


    @classmethod
    def empty_memory_buffer_options(cls):
        print()
        available_options = [cls.ADD_STR_TO_ENCRYPT.value, cls.ADD_STR_TO_DECRYPT.value, cls.EXIT.value]
        for key, value in enumerate(available_options, start=1):
            print(f"{key}. {value}")

    @classmethod
    def not_empty_memory_buffer(cls):
        print()
        for key, value in enumerate(cls, start=1):
            print(f"{key}. {value.value}")

class Suboptions(Enum):
    FROM_CONSOLE = "Wpisując ręcznie"
    FROM_FILE = "Wczytując z pliku"

    @classmethod
    def show_all(cls):
        result = []
        for key, value in enumerate(cls, start=1):
            result.append(f"{key}. {value.value}")
        result.append(Messages.CHOOSE_OPTION.value)
        return '\n'.join(result)
