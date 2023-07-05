from unittest.mock import Mock

import pytest
import tempfile

from src.filehandler import FileHandler
from src.memorybuffer import MemoryBuffer
from src.text import Text


@pytest.fixture
def mock_obj_filehandler(mocker):
    mock = Mock()
    memory_buffer = MemoryBuffer()

    txt1 = Text("Hello", "rot13", "to_encrypt")
    txt2 = Text("World", "rot47", "to_encrypt")

    memory_buffer.add_to_memory_buffer(txt1)
    memory_buffer.add_to_memory_buffer(txt2)

    mock.some_property_side_effect = memory_buffer

    return mock.some_property_side_effect


def test_prepare_save(mock_obj_filehandler, monkeypatch):
    with tempfile.NamedTemporaryFile() as tmp_file:
        inputs = iter([tmp_file.name, "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    FileHandler.prepare_save(mock_obj_filehandler)

    assert mock_obj_filehandler.memory_buffer[0].status == "encrypted"
    assert mock_obj_filehandler.memory_buffer[1].status == "encrypted"


def test_open_correct_file_input():
    result = FileHandler.open("correct_file_input.json")
    assert result == "Ala ma kota\nMaciek ma psa"


def test_open_correct_json_file_input():
    result = FileHandler.open("correct_json_file_input.json")
    assert result == [
        Text("djr", "ROT13", "encrypted"),
        Text("qwe", "ROT47", "decrypted"),
    ]


def test_override_file(mock_obj_filehandler, monkeypatch):
    inputs = iter(["json_output_file", "t", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    FileHandler.prepare_save(mock_obj_filehandler)
    assert mock_obj_filehandler.memory_buffer[-2].status == "encrypted"
    assert mock_obj_filehandler.memory_buffer[-1].status == "encrypted"
