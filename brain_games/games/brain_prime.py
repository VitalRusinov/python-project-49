from ..utils.game_base import game_base
from ..utils.generate_random_number import generate_random_number


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def get_prime_data():
    question = generate_random_number()
    answer = "yes" if is_prime(question) else "no"
    return question, answer


def brain_prime():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_base(task, get_prime_data)


if __name__ == "__main__":
    brain_prime()
