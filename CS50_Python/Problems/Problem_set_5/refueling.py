from fuel import convert, gauge
import pytest

def test_valueerror_refueling():
    with pytest.raises(ValueError):
        convert("5/4")
        convert("1.5/3")


def test_zerodivisionerror_refueling():
    with pytest.raises(ZeroDivisionError):
        convert("50/0")
        convert("0/0")


def test_profperfunctioning_refueling():
    assert convert("1/4")==25
    assert convert("3/4")==75
    assert gauge(99)=="F"
    assert gauge(1)=="E"
    assert gauge(50)=="50%"