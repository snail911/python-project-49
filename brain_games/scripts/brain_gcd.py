from random import randint
from brain_games.cli import start


def get_correct_ans_gcd():
    rand_num1, rand_num2 = randint(1, 100), randint(1, 100)
    question = f'{rand_num1} {rand_num2}'
    biggest_num = rand_num1 if rand_num1 < rand_num2 else rand_num2
    maximum = 0
    for num in range(1,biggest_num + 1):
        if rand_num1 % num == 0 and rand_num2 % num == 0:
            maximum = max(maximum, num)
    correct_answer = maximum
    return question, correct_answer


def main():
    the_game = "Find the greatest common divisor of given numbers."
    start(the_game, get_correct_ans_gcd)


if __name__ == '__main__':
    main()
