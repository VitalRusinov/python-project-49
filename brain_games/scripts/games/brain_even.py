from ..utils.game_base import game_base
from ..utils.generate_random_number import generate_random_number
from ..utils.is_even import is_even


def get_even_data():
    question = generate_random_number()
    answer = "yes" if is_even(question) else "no"
    return question, answer


def brain_even():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_base(task, get_even_data)


if __name__ == "__main__":
    brain_even()
