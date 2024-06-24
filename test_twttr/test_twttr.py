from twttr import shorten

def test_shorten():
    assert shorten("hEllo") == "hll"
    assert shorten("hE is gOd ") == 'h s gd '
    assert shorten("aaeigauo") == 'g'

def test_capital_vowel():
    assert shorten('hEllO') =='hll'

def test_numbers():
    assert shorten('hello123') == 'hll123'

def test_omit_punctuation():
    assert shorten('hello!!!') == 'hll!!!'