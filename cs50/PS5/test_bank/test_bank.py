from bank import value

def test_hello():
    assert value("Hello") == 0

def test_h():
    assert value("hi") == 20

def test_yo():
    assert value("YO") == 100