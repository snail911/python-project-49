from random import randint
from brain_games.handler_func import run


def get_correct_ans_prime():
    question = randint(1, 100)
    correct_ans = 'no'
    list_of_nums = []
    if question != 1:
        for i in range(2, question + 1):
            if question % i == 0 and i != question:
                return question, correct_ans
        correct_ans = 'yes'
        return question, correct_ans
    else:
        return question, correct_ans


def main():
    the_game = "Answer 'yes' if given number is prime. Otherwise answer 'no'."
    run(the_game, get_correct_ans_prime)


if __name__ == '__main__':
    main()
