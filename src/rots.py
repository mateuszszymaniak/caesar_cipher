class Rots:
    @staticmethod
    def rot13(txt: str) -> str:
        """
        Method encrypt/decrypt string to its representation in rot13 algorithm
        i.e. "abc" -> "nop"

        :param txt: str
        :return: txt: str
        """
        result = ""
        for letter in txt:
            if 65 <= ord(letter) <= 77 or 97 <= ord(letter) <= 109:
                result += chr(ord(letter) + 13)
            elif 78 <= ord(letter) <= 90 or 110 <= ord(letter) <= 122:
                result += chr(ord(letter) - 13)
            else:
                result += letter
        return result

    @staticmethod
    def rot47(txt: str) -> str:
        """
        Method encrypt/decrypt string to its representation in rot47 algorithm
        i.e. "abc" -> "234"

        :param txt: str
        :return: txt: str
        """
        result = ""
        for letter in txt:
            if 33 <= ord(letter) <= 81:
                result += chr(ord(letter) + 47)
            elif 82 <= ord(letter) <= 126:
                result += chr(ord(letter) - 47)
            else:
                result += letter
        return result