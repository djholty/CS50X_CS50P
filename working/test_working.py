import re
import pytest
from working import convert


def test_raiseerror():
    with pytest.raises(ValueError):
        convert('11:59 AM to 9:61 PM')

def test_12AM():
    assert convert('12 AM to 4 PM') == '00:00 to 16:00'

def test_12PM():
    assert convert('12 PM to 6 AM') == '12:00 to 06:00'

def test_regularhours():
    assert convert('8:30 PM to 10:15 PM') == '20:30 to 22:15'
    assert convert('4:20 AM to 10 AM' ) == '04:20 to 10:00'

def test_raiseValue_omits_to():
    with pytest.raises(ValueError):
        convert('9:00 AM 5 PM')

def test_raiseValue_invalidformata():
    with pytest.raises(ValueError):
        convert('8:60 AM to 4:60 PM')

def test_raiseValue_invalidformatb():
    with pytest.raises(ValueError):
        convert('9AM to 5PM')

def test_raiseValue_invalidformatc():
    with pytest.raises(ValueError):
        convert('09:00 to 17:00')