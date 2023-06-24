from enum import Enum

class Statuses(Enum):
    TO_ENCRYPT = 'to_encypt'
    TO_DECRYPT = 'to_decrypt'
    ENCRYPT = 'encrypt'
    DECRYPT = 'decrypt'

    @staticmethod
    def change_status(status):
        if status == Statuses.TO_ENCRYPT.value:
            return Statuses.ENCRYPT.value
        elif status == Statuses.TO_DECRYPT.value:
            return Statuses.DECRYPT.value
        elif status == Statuses.ENCRYPT.value:
            return Statuses.DECRYPT.value
        else:
            return Statuses.ENCRYPT.value