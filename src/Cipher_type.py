from enum import Enum

class CipherType(Enum):
    ROT13 = "ROT13"
    ROT47 = "ROT47"

    @staticmethod
    def show_all():
        for key, value in enumerate(CipherType, start=1):
            print(f"{key}. {value.value}")
