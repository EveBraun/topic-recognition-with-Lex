'Task about fractions'

class InvalidNumerator(ValueError):
    """Value must be int type"""

class InvalidDenominator(ValueError):
    """Value must be int type"""

class ZeroDenominator(ValueError):
    """Value must be int type"""

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        return f'{self.numerator} / {self.denominator}'
    
    def __repr__(self) -> str:
        return f'Fraction({self.numerator}, {self.denominator})'

    # метод для ввода данных
    def set_numerator(self, new_value: int) -> None:
        if not isinstance(new_value, int):
            raise InvalidNumerator
                     
        self.numerator = new_value

    def set_denominator(self, new_value: int) -> None:
        if not isinstance(new_value, int):
            raise InvalidNumerator
        
        if new_value == 0:
            raise ZeroDenominator
        
        self.denominator = new_value


    # Метод для сравнения 2-х дробей
    def __eq__(self, otherFraction: "Fraction") -> str:
        return (self.numerator, self.denominator) == (otherFraction.numerator, otherFraction.denominator)


