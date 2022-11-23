import prompt


def start(rule, func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(rule)
    for i in range(3):
        question,correct_ans = func()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ').lower()
        if correct_ans == answer:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name}!')
                return

        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_ans}.")
            print(f"Let's try again, {name}!")
            return
