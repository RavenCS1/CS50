from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-2)
    jar=Jar(10)
    assert jar.capacity==10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar(12)
    with pytest.raises(ValueError):
        Jar.deposit(jar,13)
    jar=Jar(6)
    Jar.deposit(jar,5)
    assert jar.size==5

def test_withdraw():
    jar=Jar(12)
    Jar.deposit(jar,11)
    with pytest.raises(ValueError):
        Jar.withdraw(jar, 12)
    jar=Jar(12)
    Jar.deposit(jar,11)
    Jar.withdraw(jar,3)
    assert jar.size==8