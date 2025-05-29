import os
import random

def validate_choice(choice, max_range):
    if choice.isdigit() and 1 <= int(choice) <= max_range:
        return True
    else:
        print(f"Invalid choice, please enter a number between 1 and {max_range}.")
        input("Press Enter to continue...")
        return False

def generate_random_id():
    return random.randint(10000, 99999)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_cursor_coordinate(x, y):
    print(f"\033[{y};{x}H", end='')
