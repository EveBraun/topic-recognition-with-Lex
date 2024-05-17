'Task about fractions'

import exeptions

class FractionOperators:
    def __mul__(self, otherFraction) -> 'Fraction':
        numerator = self.numerator * otherFraction.numerator
        denominator = self.denominator * otherFraction.denominator
        return Fraction(numerator, denominator)
    
    def mult (self, otherFraction):
        numerator = self.numerator * otherFraction.numerator
        denominator = self.denominator * otherFraction.denominator
        return Fraction(numerator, denominator)

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
            raise exeptions.InvalidNumerator
                     
        self.numerator = new_value

    def set_denominator(self, new_value: int) -> None:
        if not isinstance(new_value, int):
            raise exeptions.InvalidNumerator
        
        if new_value == 0:
            raise exeptions.ZeroDenominator
        
        self.denominator = new_value


    # Метод для сравнения 2-х дробей
    def __eq__(self, otherFraction: "Fraction") -> str:
        return (self.numerator, self.denominator) == (otherFraction.numerator, otherFraction.denominator)


