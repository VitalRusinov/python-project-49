from ..utils.game_base import game_base
from ..utils.generate_random_number import generate_random_number
from ..utils.get_gcd import get_gcd


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
