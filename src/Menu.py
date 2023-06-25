from __future__ import annotations

from src.FileHandler import *
from src.MemoryBuffer import MemoryBuffer
from src.Text import Text
from src.enums.Statuses import Statuses
from src.Cipher_type import CipherType
from src.enums.Options import *

class Menu:

    @staticmethod
    def display_menu(memory_buffer_len: int) -> None:
        """
        Method control displaying menu depends on length of memory_buffer

        :param memory_buffer_len: int
        :return: None
        """
        if memory_buffer_len == 0:
            Options.empty_memory_buffer_options()
        else:
            Options.not_empty_memory_buffer()
    @classmethod
    def show_main_menu(cls, memory_buffer: MemoryBuffer) -> None:
        """
        Method shows main menu of program

        :param memory_buffer: MemoryBuffer
        :return: None
        """
        Menu.display_menu(memory_buffer.get_length())
        option = input(Messages.CHOOSE_OPTION.value)
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
                    print(Messages.WRONG_ACTION.value)
                else:
                    memory_buffer.show_memory_buffer()
            case "5":
                if memory_buffer.get_length() == 0:
                    print(Messages.WRONG_ACTION.value)
                else:
                    print("Zamykam program")
                    exit()
            case _:
                print(Messages.WRONG_ACTION.value)

    @staticmethod
    def source_input() -> str:
        """
        Method displays suboption of methods of load data to convert and return chosen option

        :return: str
        """
        suboption = input(f"\nW jaki sposób chcesz podać tekst?\n{Suboptions.show_all()}")
        return suboption

    @classmethod
    def set_str_to_memory_buffer(cls, memory_buffer: MemoryBuffer, *args: str) -> None:
        """
        Method initialize of adding txt to encrypt/decrypt into memory_buffer

        :param memory_buffer: MemoryBuffer
        :param args: str
        :return: None
        """
        suboption = cls.source_input()
        if args[0] == Statuses.TO_ENCRYPT.value:
            match suboption:
                case '1':
                    text = input(Messages.TXT_TO_ENCODE.value)
                    rot_type = cls.chose_rot_type()
                    text_obj = Text(text, rot_type, args[0])
                    memory_buffer.add_to_memory_buffer(text_obj)
                case '2':
                    print(Messages.LOAD_FROM_FILE_TO_ENCRYPT_WARNING.value)
                    file_name = input(Messages.NAME_OF_FILE.value) + '.json'
                    try:
                        data = FileHandler.open(file_name)
                        rot_type = cls.chose_rot_type()
                        text_obj = Text(data, rot_type, args[0])
                        memory_buffer.add_to_memory_buffer(text_obj)
                    except FileNotFoundError:
                        print(Messages.FILE_NOT_EXIST.value)
                        cls.set_str_to_memory_buffer(memory_buffer, args[0])
        else:
            match suboption:
                case '1':
                    text = input(Messages.TXT_TO_DECODE.value)
                    rot_type = cls.chose_rot_type()
                    text_obj = Text(text, rot_type, args[0])
                    memory_buffer.add_to_memory_buffer(text_obj)
                case '2':
                    print(Messages.LOAD_FROM_FILE_TO_DECRYPT_WARNING.value)
                    file_name = input(Messages.NAME_OF_FILE.value) + '.json'
                    try:
                        data = FileHandler.open(file_name)
                        for obj in data:
                            obj.status = Statuses.change_status_after_load(obj.status)
                            text_obj = Text(obj.txt, obj.rot_type, obj.status)
                            memory_buffer.add_to_memory_buffer(text_obj)
                    except FileNotFoundError:
                        print(Messages.FILE_NOT_EXIST.value)
                        cls.set_str_to_memory_buffer(memory_buffer, args[0])
    @classmethod
    def chose_rot_type(cls) -> str:
        """
        Method display available rot types and allow to choose one

        :return: str
        """
        print(Messages.AVAILABLE_ROT_TYPES.value)
        CipherType.show_all()
        encrypt_option_chosen = int(input(Messages.CHOOSE_ROT_TYPE.value))
        try:
            return list(CipherType)[encrypt_option_chosen - 1].value
        except IndexError:
            print(Messages.WRONG_ACTION.value)
            cls.chose_rot_type()