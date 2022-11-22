import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while True:
        rand_number = randint(1, 100)
        print(f'Question:{rand_number}')
        answer = prompt.string('Your answer:').lower()
        correct_answer = 'yes' if rand_number % 2 == 0 else 'no'
        if correct_answer == answer:
            count += 1
            print('Correct!')
            if count == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()
