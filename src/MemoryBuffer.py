from dataclasses import asdict

class MemoryBuffer:
    memory_buffer = []

    def add_to_memory_buffer(self, text_object) -> None:
        self.memory_buffer.append(text_object)

    def memory_buffer_to_dct(self):
        return [asdict(text) for text in self.memory_buffer]