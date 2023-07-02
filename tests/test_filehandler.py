import pytest
import tempfile

from src.filehandler import FileHandler
from src.memorybuffer import MemoryBuffer
from src.text import Text


@pytest.fixture
def mock_obj_filehandler(mocker):
    memory_buffer = MemoryBuffer

    txt1 = Text("Hello", "rot13", "to_encrypt")
    txt2 = Text("World", "rot47", "to_encrypt")

    memory_buffer.add_to_memory_buffer(txt1)
    memory_buffer.add_to_memory_buffer(txt2)

    return memory_buffer.memory_buffer

def test_prepare_save(mock_obj_filehandler, monkeypatch):
    with tempfile.NamedTemporaryFile() as tmp_file:
        inputs = iter([tmp_file.name, '2'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    FileHandler.prepare_save(mock_obj_filehandler)

    assert mock_obj_filehandler[0].status == "encrypted"
    assert mock_obj_filehandler[1].status == "encrypted"