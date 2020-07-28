import typing
import unittest

from app import StringCalculator
'''

class StringCalculator:


    def add(self, user_input: str) -> int:

        if user_input is None or user_input.strip() == '':
            return 0
        
        else:
            numbers = user_input.split(',')
            result = 0
            for number in numbers:
                if number.isdigit:
                    result += int(number)
                else:
                    raise ValueError
                    print(f"ValueError:Your input is not a digit. You have to give a digits to add them.")

            return result
'''

class TestStringCalculator(unittest.TestCase):
    
    calculator = StringCalculator()

    def test_adding_one_number(self):
        self.assertEqual(self.calculator.add("2"), 2)

    def test_when_whitespace__is_given(self):
        self.assertEqual(self.calculator.add('     '), 0)

    def test_when_none_is_given(self):
        self.assertEqual(self.calculator.add(None), 0)

    def test_when_two_number_are_given(self):
        self.assertEqual(self.calculator.add("2,5"), 7)

    def test_when_input_is_not_digit(self):
        with self.assertRaises(ValueError):
            self.assertRaises(self.calculator.add("Somestring, not a digit"), 3)

    def test_when_digit_is_less_then_zero(self):
        self.assertEqual(self.calculator.add("-5,8"), 3)

    def test_when_two_digit_are_less_then_zero(self):
        self.assertEqual(self.calculator.add("-5,-8"), -13)



if __name__ == "__main__":
    unittest.main()