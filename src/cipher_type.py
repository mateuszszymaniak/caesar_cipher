from enum import Enum

from src.rots import Rots


class CipherType(Enum):
    ROT13 = "ROT13"
    ROT47 = "ROT47"

    @staticmethod
    def show_all() -> None:
        """
        Method display all available rot types

        """
        for key, value in enumerate(CipherType, start=1):
            print(f"{key}. {value.value}")
