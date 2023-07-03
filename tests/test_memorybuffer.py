from src.memorybuffer import MemoryBuffer
from src.text import Text
import pytest


@pytest.fixture
def set_mock_memorybuffer(mocker):
    my_mock = MemoryBuffer
    my_mock.memory_buffer = [Text("azx", "rot_13", "encrypted")]
    return my_mock


def test_add(set_mock_memorybuffer):
    new_obj = Text("qwe", "rot_47", "to_encrypt")
    set_mock_memorybuffer.add_to_memory_buffer(new_obj)
    assert set_mock_memorybuffer.get_length() == 2


def test_is_empty(set_mock_memorybuffer):
    assert set_mock_memorybuffer.is_empty


def test_clear_memory_buffer(set_mock_memorybuffer):
    assert set_mock_memorybuffer.clear_memory_buffer
    set_mock_memorybuffer.clear_memory_buffer()


def test_is_empty_without_mock():
    memorybuffer = MemoryBuffer
    assert memorybuffer.is_empty()
