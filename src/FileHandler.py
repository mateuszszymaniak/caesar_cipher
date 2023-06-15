import json
import os
from src.MemoryBuffer import MemoryBuffer

class FileHandler:
    @staticmethod
    def save(file_name: str):
        with open(file_name, 'w') as writer:
            json.dump(MemoryBuffer.memory_buffer_to_dict(), writer)

    @staticmethod
    def open(file_name):
        with open(file_name, 'r') as reader:
            json.load(reader)

    @staticmethod
    def prepare_save(memory_buffer: MemoryBuffer):
        file_name = input("Podaj nazwę pliku: ") + '.json'
        file_exist: bool = FileHandler.check_file(file_name)
        if file_exist: #TODO need add encrypt/decrypt text from memory_buffer
            FileHandler.override_file(file_name, memory_buffer)
        FileHandler.save(file_name)

    @staticmethod
    def check_file(file_name: str) -> bool:
        return os.path.isfile(file_name)

    @staticmethod
    def override_file(file_name: str, memory_buffer: MemoryBuffer):
        pass #TODO

