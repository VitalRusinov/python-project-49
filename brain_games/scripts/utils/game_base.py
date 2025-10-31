import prompt

def game_base(task, getData):
    total_rounds = 3
    current_round = 1

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(task)

    while current_round <= total_rounds:
        question, answer = getData()

        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(answer):
            print('Correct!')
            current_round += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
