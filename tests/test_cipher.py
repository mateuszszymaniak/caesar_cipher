from unittest.mock import Mock

import pytest

from src.cipher import Cipher
from src.memorybuffer import MemoryBuffer
from src.text import Text


@pytest.fixture
def mock_cipher_with_all_to_encrypt(mocker):
    mock = Mock()

    memory_buffer = MemoryBuffer()
    txt1 = Text("Hello", "rot13", "to_encrypt")
    txt2 = Text("(@C=5", "rot47", "to_decrypt")

    memory_buffer.add_to_memory_buffer(txt1)
    memory_buffer.add_to_memory_buffer(txt2)

    mock.some_property.side_effect = memory_buffer

    return mock.some_property.side_effect


@pytest.fixture
def mock_cipher_with_text_to_encrypt(mocker):
    mock = Mock()
    memory_buffer = MemoryBuffer()
    txt1 = Text("Hello", "rot13", "to_encrypt")
    txt2 = Text("World", "rot47", "to_encrypt")
    txt3 = Text("qwe", "rot13", "encrypted")

    memory_buffer.add_to_memory_buffer(txt1)
    memory_buffer.add_to_memory_buffer(txt2)
    memory_buffer.add_to_memory_buffer(txt3)

    mock.some_property.side_effect = memory_buffer

    return mock.some_property.side_effect


@pytest.fixture
def mock_cipher_with_no_text_to_encrypt(mocker):
    mock = Mock()
    memory_buffer = MemoryBuffer()
    memory_buffer.add_to_memory_buffer(Text("qwe", "rot13", "encrypted"))

    mock.some_property.side_effect = memory_buffer
    return mock.some_property.side_effect


@pytest.fixture
def mock_cipher_with_text_to_decrypt(mocker):
    mock = Mock()
    memory_buffer = MemoryBuffer()
    txt1 = Text("Uryyb", "rot13", "to_decrypt")
    txt2 = Text("(@C=5", "rot47", "to_decrypt")
    txt3 = Text("qwe", "rot13", "decrypted")

    memory_buffer.add_to_memory_buffer(txt1)
    memory_buffer.add_to_memory_buffer(txt2)
    memory_buffer.add_to_memory_buffer(txt3)

    mock.some_property.side_effect = memory_buffer
    return mock.some_property.side_effect


@pytest.fixture
def mock_cipher_with_no_text_to_decrypt(mocker):
    mock = Mock()
    memory_buffer = MemoryBuffer()

    memory_buffer.add_to_memory_buffer(Text("qwe", "rot13", "decrypted"))

    mock.some_property.side_effect = memory_buffer
    return mock.some_property.side_effect


def test_convert_text_rot13():
    result = Cipher.convert_text("Hello", "rot13")
    assert result == "Uryyb"


def test_convert_text_rot47():
    result = Cipher.convert_text("Hello", "rot47")
    assert result == "w6==@"


def test_convert_text_undefined_rot_type():
    result = Cipher.convert_text("Hello", "undefined")
    assert result == "Hello"


def test_convert_to_encrypt_with_valid_text(mock_cipher_with_text_to_encrypt):
    result = Cipher.convert_to_encrypt(mock_cipher_with_text_to_encrypt)

    assert result.memory_buffer[0].txt == "Uryyb"
    assert result.memory_buffer[0].status == "encrypted"
    assert result.memory_buffer[1].txt == "(@C=5"
    assert result.memory_buffer[1].status == "encrypted"
    assert result.memory_buffer[2].txt == "qwe"
    assert result.memory_buffer[2].status == "encrypted"


def test_convert_to_encrypt_with_no_valid_text(mock_cipher_with_no_text_to_encrypt):
    result = Cipher.convert(mock_cipher_with_no_text_to_encrypt, "3")

    assert result.memory_buffer[0].txt == "qwe"
    assert result.memory_buffer[0].status == "encrypted"


def test_convert_to_decrypt_with_valid_text(mock_cipher_with_text_to_decrypt):
    result = Cipher.convert_to_decrypt(mock_cipher_with_text_to_decrypt)

    assert result.memory_buffer[0].txt == "Hello"
    assert result.memory_buffer[0].status == "decrypted"
    assert result.memory_buffer[1].txt == "World"
    assert result.memory_buffer[1].status == "decrypted"
    assert result.memory_buffer[2].txt == "qwe"
    assert result.memory_buffer[2].status == "decrypted"


def test_convert_to_decrypt_with_no_valid_text(mock_cipher_with_no_text_to_decrypt):
    result = Cipher.convert_to_decrypt(mock_cipher_with_no_text_to_decrypt)

    assert result.memory_buffer[0].txt == "qwe"
    assert result.memory_buffer[0].status == "decrypted"


def test_convert_all(mock_cipher_with_all_to_encrypt):
    result = Cipher.convert(mock_cipher_with_all_to_encrypt, "1")

    assert result.memory_buffer[0].txt == "Uryyb"
    assert result.memory_buffer[0].status == "encrypted"
    assert result.memory_buffer[1].txt == "World"
    assert result.memory_buffer[1].status == "decrypted"
