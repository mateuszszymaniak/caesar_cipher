import json

class FileHandler:
    @staticmethod
    def save(file_name: str, did_override: (str, None)):
        with open(file_name, 'w') as writer:
            json.dump(asdict(self), writer)# to fix

    @staticmethod
    def open(file_name):
        with open(file_name, 'r') as reader:
            json.load(reader)

