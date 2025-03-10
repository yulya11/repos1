import random


def generate_progression():

    start = random.randint(1, 10)  
    common_ratio = random.randint(2, 5)  
    length = random.randint(5, 10) 
    progression = [start]
    for _ in range(length - 1):
        start *= common_ratio
        progression.append(start)
    return progression


def generate_question():

    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1) 
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."  
    question = " ".join(map(str, progression))  
    return question, correct_answer


def run_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    correct_answers_count = 0
    while correct_answers_count < 3:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


run_game()