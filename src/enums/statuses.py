from enum import Enum


class Statuses(Enum):
    TO_ENCRYPT = "to_encrypt"
    TO_DECRYPT = "to_decrypt"
    ENCRYPT = "encrypted"
    DECRYPT = "decrypted"

    @staticmethod
    def change_status_before_convert(status):
        if status == Statuses.TO_ENCRYPT.value:
            return Statuses.ENCRYPT.value
        elif status == Statuses.TO_DECRYPT.value:
            return Statuses.DECRYPT.value

    @staticmethod
    def change_status_after_load(status):
        if status == Statuses.ENCRYPT.value:
            return Statuses.TO_DECRYPT.value
        elif status == Statuses.DECRYPT.value:
            return Statuses.TO_ENCRYPT.value

    @staticmethod
    def revert_status_for_unused_convert(status):
        if status == Statuses.TO_DECRYPT.value:
            return Statuses.ENCRYPT.value
        elif status == Statuses.TO_ENCRYPT.value:
            return Statuses.DECRYPT.value
