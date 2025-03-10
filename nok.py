from random import randint


def gcd(a, b):
    
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):

    return (a * b) // gcd(a, b)


def game():

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")
    round = 0
    while round < 3:
        a, b, c = randint(1, 30), randint(1, 30), randint(1, 30)
        print('Question:', a, b, c)
        answer = int(input('Your answer:'))
        lcm1 = lcm(lcm(a, b), c)
        if answer == lcm1:
            print('Correct!')
            round += 1
        else:
            print(f'"{answer}" is wrong answer ; (Correct answer was "{lcm1}")')
            print(f"Let's try again, {name}!")
            break
        if round == 3:
            print(f'Congratulations, {name}!')


game()
