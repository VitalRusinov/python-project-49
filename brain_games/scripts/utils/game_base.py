import prompt

def game_base(task, get_data, total_rounds=3):

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(task)

    for _ in range(total_rounds):
        question, answer = get_data()

        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')