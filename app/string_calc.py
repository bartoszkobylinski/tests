

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
                    raise ValueError:
                    print(f"ValueError:Your input is not a digit. You have to give a digits to add them.")

            return result