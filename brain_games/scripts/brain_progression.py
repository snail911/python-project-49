from random import randint
from brain_games.handler_func import run


def get_correct_ans_progression():
    length, start, step = randint(5, 10), randint(1, 100), randint(1, 100)
    progression = [str(x) for x in range(start, (length * step) + 1, step)]
    random_index = randint(0, len(progression) - 1)
    correct_ans = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    return question,correct_ans


def main():
    the_game = "What number is missing in the progression?"
    run(the_game, get_correct_ans_progression)


if __name__ == '__main__':
    main()
