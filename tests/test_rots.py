from src.rots import Rots


def test_ro13_convert():
    txt = "abc"
    assert Rots.rot13(txt) == "nop"


def test_rot13_with_polish_characters():
    txt = "asł d"
    assert Rots.rot13(txt) == "nfł q"


def test_rot47_convert():
    txt = "kot"
    assert Rots.rot47(txt) == "<@E"


def test_rot47_with_polish_characters():
    txt = "słońce"
    assert Rots.rot47(txt) == "Dł@ń46"

