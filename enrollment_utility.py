import os
import random

generated_id =[]
def validate_choice(choice, max_range):
    if choice.isdigit() and 1 <= int(choice) <= max_range:
        return True
    else:
        set_cursor_coordinate(10, 15)
        print(f"Invalid choice, please enter a number between 1 and {max_range}.")
        set_cursor_coordinate(10, 16)
        input("Press Enter to continue...")
        return False

def generate_random_id():
    gen_id = random.randint(10000, 99999)
    while True:
        if gen_id not in generated_id:
            generated_id.append(gen_id)
            return gen_id

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_cursor_coordinate(x, y):
    print(f"\033[{y};{x}H", end='')

def load_quiz_id(quizzes):
    for quiz in quizzes:
        generated_id.append(quiz)
