from dataclasses import dataclass, asdict
from typing import Any

from src.text import Text


class MemoryBuffer:
    memory_buffer = []

    @classmethod
    def get_length(cls) -> int:
        """
        Method returns length of memory_buffer

        :return: int
        """
        return len(cls.memory_buffer)

    @classmethod
    def add_to_memory_buffer(cls, text_object: Text) -> None:
        """
        Method add Text object into memory_buffer

        :param text_object: Text
        :return: None
        """
        cls.memory_buffer.append(text_object)

    @classmethod
    def insert_to_memory_buffer(cls, text_object: Text, position: int) -> list[Any]:
        """
        Method insert Text object in position to memory_buffer

        :param text_object: Text
        :param position: int
        :return: list[Any]
        """
        cls.memory_buffer.insert(position, text_object)
        return cls.memory_buffer

    @classmethod
    def memory_buffer_to_dict(cls) -> list[dict[str, Any]]:
        """
        Method convert list memory_buffer into dict

        :return: dict
        """
        return [asdict(text) for text in cls.memory_buffer]

    @classmethod
    def show_memory_buffer(cls) -> None:
        """
        Method display objects from memory_buffer

        :return: None
        """
        for idx, item in enumerate(cls.memory_buffer, start=1):
            print(f"{idx}. {item}")

    @classmethod
    def clear_memory_buffer(cls) -> None:
        """
        Method clear memory_buffer

        :return: None
        """
        cls.memory_buffer.clear()

    @classmethod
    def is_empty(cls) -> bool:
        return len(cls.memory_buffer) == 0
