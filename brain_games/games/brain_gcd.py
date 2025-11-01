from ..utils.game_base import game_base
from ..utils.generate_random_number import generate_random_number


def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def get_gcd_data():
    num1 = generate_random_number()
    num2 = generate_random_number()

    question = f"{num1} {num2}"
    answer = get_gcd(num1, num2)

    return question, answer


def brain_gcd():
    task = "Find the greatest common divisor of given numbers."
    game_base(task, get_gcd_data)


if __name__ == "__main__":
    brain_gcd()
