from ..utils.generate_random_number import generate_random_number
from ..utils.game_base import game_base
from ..utils.get_progression import get_progression

MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
MIN_INDEX = 0

def get_progression_data():
    progression = get_progression(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    length = len(progression) - 1
    hidden_index = generate_random_number(MIN_INDEX, length - 1)

    answer = progression[hidden_index]

    progression[hidden_index] = ".."

    question = ' '.join(progression)

    return question, answer

def brain_progression():
    task = 'What number is missing in the progression?'
    game_base(task, get_progression_data)

if __name__ == "__main__":
    brain_progression()