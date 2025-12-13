from plates import is_valid

def test_first_two_letter_plates():
    assert is_valid("K1")==False
    assert is_valid("1T")==False
    assert is_valid("AA")==True

def test_len_plates():
    assert is_valid("K")==False
    assert is_valid("KABCDEF")==False
    assert is_valid("KAT")==True


def test_numbers_plates():
    assert is_valid("KK10K")==False
    assert is_valid("CS50")==True
    assert is_valid("KK01")==False

def test_punctuation_plates():
    assert is_valid("KK50,")==False
    assert is_valid("CS.50")==False