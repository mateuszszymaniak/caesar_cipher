import json
import os
from src.MemoryBuffer import MemoryBuffer
from src.Text import Text
from src.Cipher import Cipher

class FileHandler:
    @staticmethod
    def save(file_name: str):
        with open(file_name, 'w', encoding='utf-8') as writer:
            json.dump(MemoryBuffer.memory_buffer_to_dict(), writer, ensure_ascii=False)

    @staticmethod
    def open(file_name):
        result = []
        with open(file_name, 'r', encoding='utf-8') as reader:
            data = json.load(reader)
        for i in data:
            if len(i.keys()) == 1:
                return i['txt']
            else:
                text_obj = Text(i['txt'], i['rot_type'], i['status'])
                result.append(text_obj)
        return result

    @staticmethod
    def prepare_save(memory_buffer: MemoryBuffer):
        file_name = input("Podaj nazwę pliku: ") + '.json'
        if file_name == ".json":
            print("Podano pustą nazwę pliku!")
            FileHandler.prepare_save(memory_buffer)
        file_exist: bool = FileHandler.check_file(file_name)
        if file_exist: #TODO need add encrypt/decrypt text from memory_buffer
            FileHandler.override_file(file_name, memory_buffer)
        Cipher.convert(memory_buffer)
        FileHandler.save(file_name)
        MemoryBuffer.clear_memory_buffer()

    @staticmethod
    def check_file(file_name: str) -> bool:
        return os.path.isfile(file_name)

    @staticmethod
    def override_file(file_name: str, memory_buffer: MemoryBuffer):
        choice = input("Podana nazwa pliku istnieje. Czy dopisać do pliky? [t/n]: ")
        if choice == 't':
            memory_buffer = FileHandler.append(file_name, memory_buffer)
        return memory_buffer

    @staticmethod
    def append(file_name: str, memory_buffer):
        data = FileHandler.open(file_name)
        for key, value in enumerate(data):
            memory_buffer = MemoryBuffer.insert_to_memory_buffer(value, key)
        return memory_buffer
