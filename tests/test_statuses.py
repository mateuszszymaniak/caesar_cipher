from src.enums.statuses import Statuses


def test_change_status_before_convert_to_encrypt():
    status = "to_encrypt"
    assert Statuses.change_status_before_convert(status) == "encrypted"


def test_change_status_before_convert_to_decrypt():
    status = "to_decrypt"
    assert Statuses.change_status_before_convert(status) == "decrypted"


def test_change_status_after_load_encrypt():
    status = "encrypted"
    assert Statuses.change_status_after_load(status) == "to_decrypt"


def test_change_status_after_load_decrypt():
    status = "decrypted"
    assert Statuses.change_status_after_load(status) == "to_encrypt"


def test_revert_status_for_unused_convert_to_decrypt():
    status = "to_decrypt"
    assert Statuses.revert_status_for_unused_convert(status) == "encrypted"


def test_revert_status_for_unused_convert_to_encrypt():
    status = "to_encrypt"
    assert Statuses.revert_status_for_unused_convert(status) == "decrypted"


def test_revert_status_for_unused_convert_encrypt():
    status = "encrypted"
    assert Statuses.revert_status_for_unused_convert(status) == "encrypted"


def test_revert_status_for_unused_convert_decrypt():
    status = "decrypted"
    assert Statuses.revert_status_for_unused_convert(status) == "decrypted"
