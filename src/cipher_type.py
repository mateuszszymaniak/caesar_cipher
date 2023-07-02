from enum import Enum

from src.rots import Rots


class CipherType(Enum):
    @staticmethod
    def show_all() -> None:
        """
        Method display all available rot types from rots class

        :return: None
        """
        available_ciphers = [a for a in dir(Rots) if "rot" in a]
        for key, value in enumerate(available_ciphers, start=1):
            print(f"{key}. {value.upper()}")
