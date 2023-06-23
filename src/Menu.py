from __future__ import annotations

import src.enums.Options
from src.FileHandler import *
from src.MemoryBuffer import MemoryBuffer
from src.Text import Text
from src.Statuses import Statuses
from src.Cipher_type import CipherType
from src.enums.Messages import Messages
from src.enums.Options import *

class Menu:

    @staticmethod
    def display_menu(memory_buffer_len: int) -> None:
        if memory_buffer_len == 0:
            Options.empty_memory_buffer_options()
        else:
            Options.not_empty_memory_buffer()
    @classmethod
    def show_main_menu(cls, memory_buffer):
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
    def source_input():
        #src.enums.Options.Suboptions.show_all()
        suboption = input(f"\nW jaki sposób chcesz podać tekst?\n{Suboptions.show_all()}")
        return suboption

    @classmethod
    def set_str_to_memory_buffer(cls, memory_buffer: MemoryBuffer, *args: str) -> None:
        suboption = cls.source_input()
        match suboption:
            case '1':
                text = input(Messages.TXT_TO_ENCODE.value if args[0] == Statuses.TO_ENCRYPT.value else Messages.TXT_TO_DECODE.value)
                rot_type = cls.chose_rot_type()
                text_obj = Text(text, rot_type, args[0])
                memory_buffer.add_to_memory_buffer(text_obj)
            case '2':
                print(Messages.LOAD_FROM_FILE_WARNING.value)
                file_name = input(Messages.NAME_OF_FILE.value) + '.json'
                if FileHandler.check_file(file_name):
                    data = FileHandler.open(file_name)
                    rot_type = cls.chose_rot_type()
                    text_obj = Text(data, rot_type, args[0])
                    memory_buffer.add_to_memory_buffer(text_obj)
                else:
                    print(Messages.FILE_NOT_EXIST.value)
                    cls.set_str_to_memory_buffer(memory_buffer, args[0])

    @classmethod
    def chose_rot_type(cls) -> str:
        print(f"{Messages.AVAILABLE_ROT_TYPES.value}")
        CipherType.show_all()
        encrypt_option_chosen = int(input(Messages.CHOOSE_ROT_TYPE.value))
        if list(CipherType)[encrypt_option_chosen - 1]:
            return list(CipherType)[encrypt_option_chosen - 1].value
        else:
            print(Messages.WRONG_ACTION.value)
            cls.chose_rot_type()

    @classmethod
    def get_file_name(cls) -> tuple[str, (str, None)]:
        did_add_to_file = None
        file_name = input(Messages.NAME_OF_FILE.value) + '.json'
        if os.path.isfile(file_name):
            did_add_to_file = input(Messages.OVERRIDE_FILE.value)
            if did_add_to_file == 't':
                did_add_to_file = 't'
            elif did_add_to_file == 'n':
                cls.get_file_name()
            else:
                print(Messages.WRONG_ACTION.value)
                cls.get_file_name()
        return file_name, did_add_to_file

    @classmethod
    def save_to_file_question(cls, memory_buffer: MemoryBuffer, rot_tyoe: str, status: str):
        answer = input(Messages.SAVE_TO_FILE_QUESTION.value).lower()
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
            print(Messages.WRONG_ACTION.value)
            cls.save_to_file_question(memory_buffer)