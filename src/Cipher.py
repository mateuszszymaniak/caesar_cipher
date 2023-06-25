from src.MemoryBuffer import MemoryBuffer
from src.enums.Statuses import Statuses
class Cipher:

    @staticmethod
    def rot13(txt: str) -> str:
        """
        Method encrypt/decrypt string to its representation in rot13 algorithm
        i.e. "abc" -> "nop"

        :param txt: str
        :return: txt: str
        """
        result = ""
        for letter in txt:
            if 65 <= ord(letter) <= 77 or 97 <= ord(letter) <= 109:
                result += chr(ord(letter) + 13)
            elif 78 <= ord(letter) <= 90 or 110 <= ord(letter) <= 122:
                result += chr(ord(letter) - 13)
            else:
                result += letter
        return result

    @staticmethod
    def rot47(txt: str) -> str:
        """
        Method encrypt/decrypt string to its representation in rot47 algorithm
        i.e. "abc" -> "234"

        :param txt: str
        :return: txt: str
        """
        result = ""
        for letter in txt:
            if 33 <= ord(letter) <= 81:
                result += chr(ord(letter) + 47)
            elif 82 <= ord(letter) <= 126:
                result += chr(ord(letter) - 47)
            else:
                result += letter
        return result

    @classmethod
    def convert(cls, memory_buffer, convert_option):
        """
        Method which control which text conversion use

        :param memory_buffer:
        :param convert_option:
        :return: memory_buffer
        """
        match convert_option:
            case '1':
                memory_buffer = cls.convert_all(memory_buffer)
            case '2':
                memory_buffer = cls.convert_to_encrypt(memory_buffer)
            case '3':
                memory_buffer = cls.convert_to_decrypt(memory_buffer)
        return memory_buffer

    @classmethod
    def convert_all(cls, memory_buffer):
        """
        Method convert decryt/encrypt text for all objects in memory_buffer

        :param memory_buffer:
        :return: memory_buffer
        """
        for obj in MemoryBuffer.memory_buffer:
            obj.txt = cls.convert_text(obj.txt, obj.rot_type)
            obj.status = Statuses.change_status_before_convert(obj.status)
        return memory_buffer

    @classmethod
    def convert_to_encrypt(cls, memory_buffer):
        """
        Method convert only this objects which status is 'to_encrypt'

        :param memory_buffer:
        :return: memory_buffer
        """
        for obj in MemoryBuffer.memory_buffer:
            if obj.status == 'to_encrypt':
                obj.txt = cls.convert_text(obj.txt, obj.rot_type)
                obj.status = Statuses.change_status_before_convert(obj.status)
            else:
                obj.status = Statuses.revert_status_for_unused_convert(obj.status)
        return memory_buffer

    @classmethod
    def convert_to_decrypt(cls, memory_buffer):
        """
        Method convert only this objects which status is 'to_decrypt'

        :param memory_buffer:
        :return: memory_buffer
        """
        for obj in MemoryBuffer.memory_buffer:
            if obj.status == 'to_decrypt':
                obj.txt = cls.convert_text(obj.txt, obj.rot_type)
                obj.status = Statuses.change_status_before_convert(obj.status)
            else:
                obj.status = Statuses.revert_status_for_unused_convert(obj.status)
        return memory_buffer

    @staticmethod
    def convert_text(txt, rot_type):
        """
        Method which convert text using given rot_type

        :param txt:
        :param rot_type:
        :return:
        """
        match rot_type.lower():
            case 'rot13':
                txt = Cipher.rot13(txt)
            case 'rot47':
                txt = Cipher.rot47(txt)
        return txt