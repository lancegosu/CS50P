from twttr import shorten

def test_lowercase():
    assert shorten("vlad will win his match today") == "vld wll wn hs mtch tdy"
    assert shorten("lance") == "lnc"
    assert shorten("python is cool") == "pythn s cl"
    assert shorten("abc") == "bc"

def test_uppercase():
    assert shorten("LANCE") == "LNC"

def test_novowel():
    assert shorten("lnc") == "lnc"

def test_numbers():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("hello, world.") == ("hll, wrld.")