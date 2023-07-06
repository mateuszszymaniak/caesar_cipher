from dataclasses import dataclass, asdict
from typing import Any

from src.text import Text


class MemoryBuffer:
    def __init__(self):
        self.memory_buffer = []

    def get_length(self) -> int:
        """
        Method returns length of memory_buffer
        """
        return len(self.memory_buffer)

    def add_to_memory_buffer(self, text_object: Text) -> None:
        """
        Method add Text object into memory_buffer
        """
        self.memory_buffer.append(text_object)

    def insert_to_memory_buffer(self, text_object: Text, position: int) -> list[Any]:
        """
        Method insert Text object in position to memory_buffer
        """
        self.memory_buffer.insert(position, text_object)
        return self.memory_buffer

    def memory_buffer_to_dict(self) -> list[dict[str, Any]]:
        """
        Method convert list memory_buffer into dict
        """
        return [asdict(text) for text in self.memory_buffer]

    def show_memory_buffer(self) -> None:
        """
        Method display objects from memory_buffer
        """
        for idx, item in enumerate(self.memory_buffer, start=1):
            print(f"{idx}. {item}")

    def clear_memory_buffer(self) -> None:
        """
        Method clear memory_buffer
        """
        self.memory_buffer.clear()

    def is_empty(self) -> bool:
        return len(self.memory_buffer) == 0
