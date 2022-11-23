import prompt
from random import randint, choice
import operator
from brain_games.cli import start


def get_correct_ans():
    rand_num1, rand_num2 = randint(1, 100), randint(1, 100)
    operations = {'-': operator.sub, '+': operator.add, '*': operator.mul, '/': operator.truediv}
    rand_operation = choice([x for x in operations.keys()])
    question = f'{rand_num1} {rand_operation} {rand_num2}'
    correct_answer = str(operations[rand_operation](rand_num1, rand_num2))
    return question,correct_answer


def main():
    the_game = 'What is the result of the expression?'
    start(the_game,get_correct_ans)


if __name__ == '__main__':
    main()
