
from vector import Fraction

def test_eq_1():
    f1 = Fraction(1, 1)
    f2 = Fraction(1, 1)

    assert f1 == f2


def test_eq_2():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 1)

    assert f1 != f2

def test_eq_3():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 1)

    assert f1 == f2