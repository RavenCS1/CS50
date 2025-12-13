from numb3rs import validate

def test_toobig():
    assert validate("1.2.256.0")==False
    assert validate("4.750.1.5")==False
    assert validate("601.2.3.4")==False
    assert validate("1.2.3.900")==False

def test_attributeerror():
    assert validate("1.2.3.1000")==False
    assert validate("601.2.3.4.4")==False
    assert validate("601.")==False
    assert validate("2.3,4.1")==False 
    assert validate("cat") ==False

def test_appropriate():
    assert validate("255.255.255.255")==True
    assert validate("0.0.0.0")==True
    