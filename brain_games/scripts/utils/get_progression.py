from .generate_random_number import generate_random_number

MIN_STEP, MAX_STEP = 1, 10


def get_progression(min_length, max_length):
    length = generate_random_number(min_length, max_length)
    start = generate_random_number()
    step = generate_random_number(MIN_STEP, MAX_STEP)

    return [str(start + i * step) for i in range(length)]
