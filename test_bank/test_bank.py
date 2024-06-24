import bank

def test_return0():
    assert bank.value("hellocat") == 0
    assert bank.value("hello cat") == 0
    assert bank.value("HELLO cat") == 0
def test_return20():
    assert bank.value("helicat") == 20
    assert bank.value("HOLA senior") == 20

def test_return100():
    assert bank.value('adding machine') == 100
    assert bank.value('monkeypox') == 100

def test_casesensitive():
    assert bank.value('ADDING MACHINE') == 100
    assert bank.value('Whats up') == 100