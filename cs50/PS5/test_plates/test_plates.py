from plates import is_valid

def test_size():
    assert is_valid("AA12345") == False

def test_starts():
    assert is_valid("B12345") == False

def test_numbers():
    assert is_valid("CC12C4") == False

def test_zero():
    assert is_valid("DD0123") == False

def test_special():
    assert is_valid("EE123!") == False