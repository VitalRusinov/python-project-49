import prompt

from .generate_random_number import generate_random_number
from .isEven import isEven


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    total_rounds = 3
    current_round = 1

    while current_round <= total_rounds:
        question_number = generate_random_number()
        correct_answer = 'yes' if isEven(question_number) else 'no'

        print(f"Question: {question_number}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print('Correct!')
            current_round += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()