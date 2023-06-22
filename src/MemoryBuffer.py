from dataclasses import dataclass, asdict
from src.Text import Text

class MemoryBuffer:
    memory_buffer = []

    @classmethod
    def get_length(cls):
        return len(cls.memory_buffer)
    @classmethod
    def add_to_memory_buffer(cls, text_object) -> None:
        cls.memory_buffer.append(text_object)

    @classmethod
    def insert_to_memory_buffer(cls, text_object, position) -> None:
        cls.memory_buffer.insert(position, text_object)

    @classmethod
    def memory_buffer_to_dict(cls):
        return [asdict(text) for text in cls.memory_buffer]

    @classmethod
    def show_memory_buffer(cls):
        for item in cls.memory_buffer:
            print(item)

    @classmethod
    def clear_memory_buffer(cls):
        cls.memory_buffer.clear()