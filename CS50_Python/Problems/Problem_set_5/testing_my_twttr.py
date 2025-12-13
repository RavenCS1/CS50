from twttr import shorten
import pytest

def test_lower_shorten():
    assert shorten("naeiouWm")=="nWm"

def test_upper_shorten():
    assert shorten("nAEIOUwM")=="nwM"


