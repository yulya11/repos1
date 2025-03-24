import random
from engine import run_game

def generate_question():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer

def generate_progression():
    start = random.randint(1, 10)
    common_ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = [start]
    for _ in range(length - 1):
        start *= common_ratio
        progression.append(start)
    return progression

def play():
    run_game("What number is missing in the progression?", generate_question)

if __name__ == "__main__":
    play()