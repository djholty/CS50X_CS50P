from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪"*5

def test_deposit():
    jar = Jar()
    jar.deposit(12)
    assert jar._size == 12

def test_overdeposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(12)
    assert jar._size == 0

def test_overdrawn():
    jar = Jar()
    jar.deposit(4)
    with pytest.raises(ValueError):
        jar.withdraw(5)