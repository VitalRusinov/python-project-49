from ..utils.generate_random_number import generate_random_number
from ..utils.is_prime import is_prime
from ..utils.game_base import game_base

def get_prime_data():
    question = generate_random_number()
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer

def brain_prime():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_base(task, get_prime_data)

if __name__ == "__main__":
    brain_prime()