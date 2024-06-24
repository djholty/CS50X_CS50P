
from plates import is_valid
import pytest

def test_apprpunc():
    assert is_valid("aaaaaa") == True
    assert is_valid("a aaa") == False
    assert is_valid("a!aaa") == False
    assert is_valid("a?aaa") == False
    assert is_valid("a-aaa") == False


def test_starttwo():
    assert is_valid("as332") == True
    assert is_valid('00asd') == False

def test_is_valid():
    assert is_valid("a!!!") == False
    assert is_valid("12aaa") == False
    assert is_valid("a") == False
    assert is_valid("aaaaaaa") == False
    assert is_valid("aa01") == False
    assert is_valid("aa11a") == False
    assert is_valid("aa111") == True

def test_is_valid_apprnums():
    assert is_valid('aa0123') == False
    assert is_valid('aa123') == True
    assert is_valid('aa123a') == False

def test_is_valid_platelen():
    assert is_valid("aa") == True
    assert is_valid("aaaaaa") == True
    assert is_valid("a") == False
    assert is_valid("aaaaaaa") == False

def test_number_at_start():
    assert is_valid("1ABC") == False
    assert is_valid("12ABC") == False

def test_valid_numbers2(): # test numbers at end
    assert is_valid('AAA20A') == False
def test_valid_alphanumberics(): # test zero is not first number
    assert is_valid('"CD^£%') == False

def test_isalpha_numeric():
    assert is_valid(".!@#$%") == False

def test_starttwolet():
    assert is_valid("12ABC") == False
    assert is_valid(". !??") == False

def test_CS50():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P2") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("123456") == False