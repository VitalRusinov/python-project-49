from ..utils.generate_random_number import generate_random_number
from ..utils.gameBase import gameBase

OPERATIONS = [
    ('+', lambda a, b: a + b),
    ('-', lambda a, b: a - b),
    ('*', lambda a, b: a * b)
]

OPERATOR_INDEX_RANGE = (0, len(OPERATIONS) - 1)

def get_calc_data():
    num1 = generate_random_number()
    num2 = generate_random_number()
    operator_index = generate_random_number(*OPERATOR_INDEX_RANGE)
    operator, operation = OPERATIONS[operator_index]

    question = f'{num1} {operator} {num2}'
    answer = operation(num1, num2)

    return question, answer

def brain_calc():
    task = 'What is the result of the expression?'
    gameBase(task, get_calc_data)

if __name__ == "__main__":
    brain_calc()