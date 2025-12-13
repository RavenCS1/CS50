from seasons import validate
from datetime import date

def test_validate():
    assert validate("2024-02-29")==date(2024, 2, 29)
    assert validate("1991-1-1")==date(1991, 1, 1)
    assert validate("2000-12-31")==date(2000, 12, 31)

