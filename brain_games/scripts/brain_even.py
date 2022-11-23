from random import randint
from brain_games.handler_func import run

def get_correct_ans_even():
    question = randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question,correct_answer


def main():
    the_game = "Answer 'yes' if the number is even, otherwise answer 'no'"
    run(the_game, get_correct_ans_even)


if __name__ == '__main__':
    main()
