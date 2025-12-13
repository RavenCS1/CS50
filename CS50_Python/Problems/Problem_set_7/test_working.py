from working import convert
import pytest

def test_attributeerror():
    with pytest.raises(ValueError):
        convert("9 Am 5 Pm")
        convert("10 AM 8 PM")
        convert("11 am 7 pm")
        convert("11 AM 7 PM")
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")
        convert("9AM 5PM")
        convert("9 AM 5 PM")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
        convert("12:60 AM to 6:00 PM")
        convert("9:00 AM to 12:00 PM")
        convert("9:00 AM to 12:60 PM")

def test_appropriate():
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9:00 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9 AM to 5:00 PM")=="09:00 to 17:00"
