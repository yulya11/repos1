from random import randint
from math import gcd
from engine import run_game

def generate_question():
    a, b, c = randint(1, 30), randint(1, 30), randint(1, 30)
    lcm1 = lcm(lcm(a, b), c)
    question = f"{a} {b} {c}"
    return question, str(lcm1)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def play():
    run_game("Find the smallest common multiple of given numbers.", generate_question)

if __name__ == "__main__":
    play()