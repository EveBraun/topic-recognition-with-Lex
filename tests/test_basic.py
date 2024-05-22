from vector import Fraction
import exeptions
import pytest

def test_init():
    f = Fraction(1, 2)

    assert f.numerator == 1
    assert f.denominator == 2

class TestSetNumerator:
    def test_set_numerator_correct(self):
        f = Fraction(1, 2)
        f.set_numerator(5)

        assert f.numerator == 5

    def test_set_numerator_exeption_1(self):
        f = Fraction(1, 2)
        f.set_numerator(5.0)

        with pytest.raises(exeptions.InvalidNumerator):
            f.set_numerator(5.0)