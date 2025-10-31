from ..utils.generate_random_number import generate_random_number
from ..utils.isEven import isEven
from ..utils.gameBase import gameBase

def getEvenData():
    question = generate_random_number()
    answer = 'yes' if isEven(question) else 'no'
    return question, answer

def brain_even():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    gameBase(task, getEvenData)

if __name__ == "__main__":
    brain_even()