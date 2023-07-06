from src.memorybuffer import MemoryBuffer
from src.enums.statuses import Statuses
from src.rots import Rots


class Cipher:
    @classmethod
    def convert(cls, memory_buffer: MemoryBuffer, convert_option: str) -> MemoryBuffer:
        """
        Method which control which text conversion use

        """
        match convert_option:
            case "1":
                memory_buffer = cls.convert_all(memory_buffer)
            case "2":
                memory_buffer = cls.convert_to_encrypt(memory_buffer)
            case "3":
                memory_buffer = cls.convert_to_decrypt(memory_buffer)
        return memory_buffer

    @classmethod
    def convert_all(cls, memory_buffer: MemoryBuffer) -> MemoryBuffer:
        """
        Method convert decryt/encrypt text for all objects in memory_buffer

        """
        for obj in memory_buffer.memory_buffer:
            obj.txt = cls.convert_text(obj.txt, obj.rot_type)
            obj.status = Statuses.change_status_before_convert(obj.status)
        return memory_buffer

    @classmethod
    def convert_to_encrypt(cls, memory_buffer: MemoryBuffer) -> MemoryBuffer:
        """
        Method convert only this objects which status is 'to_encrypt'

        """
        for obj in memory_buffer.memory_buffer:
            if obj.status == "to_encrypt":
                obj.txt = cls.convert_text(obj.txt, obj.rot_type)
                obj.status = Statuses.change_status_before_convert(obj.status)
            else:
                obj.status = Statuses.revert_status_for_unused_convert(obj.status)
        return memory_buffer

    @classmethod
    def convert_to_decrypt(cls, memory_buffer: MemoryBuffer) -> MemoryBuffer:
        """
        Method convert only this objects which status is 'to_decrypt'

        """
        for obj in memory_buffer.memory_buffer:
            if obj.status == "to_decrypt":
                obj.txt = cls.convert_text(obj.txt, obj.rot_type)
                obj.status = Statuses.change_status_before_convert(obj.status)
            else:
                obj.status = Statuses.revert_status_for_unused_convert(obj.status)
        return memory_buffer

    @staticmethod
    def convert_text(txt: str, rot_type: str) -> str:
        """
        Method which convert text using given rot_type

        """
        match rot_type.lower():
            case "rot13":
                txt = Rots.rot13(txt)
            case "rot47":
                txt = Rots.rot47(txt)
        return txt
