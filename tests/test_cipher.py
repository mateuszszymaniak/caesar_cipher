from unittest.mock import MagicMock

import pytest

from src.cipher import Cipher
from src.memorybuffer import MemoryBuffer
from src.text import Text


@pytest.fixture
def mock_cipher_with_text_to_encrypt(mocker):
    my_mock = MemoryBuffer
    txt1 = Text("Hello", 'rot13', 'to_encrypt')
    txt2 = Text("World", 'rot47', 'to_encrypt')
    txt3 = Text("qwe", 'rot13', 'encrypted')

    my_mock.add_to_memory_buffer(txt1)
    my_mock.add_to_memory_buffer(txt2)
    my_mock.add_to_memory_buffer(txt3)

    return my_mock


@pytest.fixture
def mock_cipher_with_no_text_to_encrypt(mocker):
    my_mock = MemoryBuffer

    txt = Text("qwe", 'rot13', 'encrypted')

    my_mock.add_to_memory_buffer(txt)
    return my_mock

@pytest.fixture
def mock_cipher_with_text_to_decrypt(mocker):
    my_mock = MemoryBuffer
    txt1 = Text("Uryyb", 'rot13', 'to_decrypt')
    txt2 = Text("(@C=5", 'rot47', 'to_decrypt')
    txt3 = Text("qwe", 'rot13', 'decrypted')

    my_mock.add_to_memory_buffer(txt1)
    my_mock.add_to_memory_buffer(txt2)
    my_mock.add_to_memory_buffer(txt3)

    return my_mock

@pytest.fixture
def mock_cipher_with_no_text_to_decrypt(mocker):
    my_mock = MemoryBuffer

    txt = Text("qwe", 'rot13', 'decrypted')

    my_mock.add_to_memory_buffer(txt)
    return my_mock


def test_convert_text_rot13():
    result = Cipher.convert_text("Hello", "rot13")
    assert result == "Uryyb"

def test_convert_text_rot47():
    result = Cipher.convert_text("Hello", "rot47")
    assert result == "w6==@"

def test_convert_text_undefined_rot_type():
    result = Cipher.convert_text("Hello", 'undefined')
    assert result == "Hello"

def test_convert_to_encrypt_with_valid_text(mock_cipher_with_text_to_encrypt):
    result = Cipher.convert_to_encrypt(mock_cipher_with_text_to_encrypt)

    assert result.memory_buffer[0].txt == "Uryyb"
    assert result.memory_buffer[0].status == "encrypted"
    assert result.memory_buffer[1].txt == "(@C=5"
    assert result.memory_buffer[1].status == "encrypted"
    assert result.memory_buffer[2].txt == "qwe"
    assert result.memory_buffer[2].status == "encrypted"

    result.clear_memory_buffer()

def test_convert_to_encrypt_with_no_valid_text(mock_cipher_with_no_text_to_encrypt):
    result = Cipher.convert_to_decrypt(mock_cipher_with_no_text_to_encrypt)

    assert result.memory_buffer[0].txt == "qwe"
    assert result.memory_buffer[0].status == "encrypted"

    result.clear_memory_buffer()

def test_convert_to_decrypt_with_valid_text(mock_cipher_with_text_to_decrypt):
    result = Cipher.convert_to_decrypt(mock_cipher_with_text_to_decrypt)

    assert result.memory_buffer[0].txt == "Hello"
    assert result.memory_buffer[0].status == "decrypted"
    assert result.memory_buffer[1].txt == "World"
    assert result.memory_buffer[1].status == "decrypted"
    assert result.memory_buffer[2].txt == "qwe"
    assert result.memory_buffer[2].status == "decrypted"

    result.clear_memory_buffer()

def test_convert_to_decrypt_with_no_valid_text(mock_cipher_with_no_text_to_decrypt):
    result = Cipher.convert_to_encrypt(mock_cipher_with_no_text_to_decrypt)

    assert result.memory_buffer[0].txt == "qwe"
    assert result.memory_buffer[0].status == "decrypted"

    result.clear_memory_buffer()