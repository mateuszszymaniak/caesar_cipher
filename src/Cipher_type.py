from enum import Enum


class CipherType(Enum):
    ROT13 = "ROT13"
    ROT47 = "ROT47"

    @staticmethod
    def show_all() -> None:
        """
        Method display all available rot types

        :return: None
        """
        for key, value in enumerate(CipherType, start=1):
            print(f"{key}. {value.value}")
