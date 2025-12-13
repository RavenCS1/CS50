from bank import value

def test_hello_bank():
    assert value("Hello")==0
    assert value("hello")==0

def test_h_bank():
    assert value("Hey how's it going")==20
    assert value("how are you?")==20

def test_withouth_bank():
    assert value("What's going on")==100
    assert value("good morning")==100
    assert value("Good afternoon")==100
    assert value("good night")==100
