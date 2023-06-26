from src.MemoryBuffer import MemoryBuffer
from src.Menu import Menu


def main():
    memory_buffer = MemoryBuffer
    print("Szyfr Cezara (ROT13/ROT47)")

    while True:
        Menu.show_main_menu(memory_buffer)


if __name__ == "__main__":
    main()
