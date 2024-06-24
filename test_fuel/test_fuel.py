import fuel
import pytest
"""hello friend"""



def test_convert_zerodivision():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")
def test_convert_value():
    with pytest.raises(ValueError):
        fuel.convert("5/4")
        fuel.convert('cat/dog')

def test_gauge():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) =="E"
    assert fuel.gauge(50) == "50%"

def test_both():
    assert fuel.convert('1/2') == 50 and fuel.gauge(50) == '50%'
    assert fuel.convert('1/1') == 100 and fuel.gauge(100) == 'F'
    assert fuel.convert('0/2') == 0 and fuel.gauge(0) == 'E'

