from enum import Enum

class Messages(Enum):
    CHOOSE_OPTION = "Wybierz opcję: "
    WRONG_ACTION = "Wybrano nieprawidłową akcję!"
    SAVE_TO_FILE_QUESTION = "Czy zapisać do pliku? [t/n]: "
    TXT_TO_ENCODE = "\nPodaj napis do zaszyfrowania: "
    TXT_TO_DECODE = "\nPodaj napis do odszyfrowania: "
    NAME_OF_FILE = "\nPodaj nazwę pliku: "
    LOAD_FROM_FILE_TO_ENCRYPT_WARNING = """Wczytany plik powinien mieć rozszerzenie .json i posiadać następującą strukturę
    
    [{"txt": "tekst do odszyfrowania/zaszyfrowania"}]
    """
    LOAD_FROM_FILE_TO_DECRYPT_WARNING = """Wczytany plik powinien mieć rozszerzenie .json i posiadać następującą strukturę
    
    [{"txt": "tekst do odszyfrowania/zaszyfrowania", "rot_type": "rodzaj szyfrowania", "status": "status"}]
    """
    FILE_NOT_EXIST = "Podany plik nie istnieje"
    AVAILABLE_ROT_TYPES = "\nDostępne rodzaje szyfrowań"
    CHOOSE_ROT_TYPE = "Wybierz rodzaj szyfrowania: "
    OVERRIDE_FILE = "Podany plik istnieje. Czy chcesz dodać zawartość do pliku? [t/n]: "
    WHAT_TO_CONVERT = "\nCo ma zrobić?"