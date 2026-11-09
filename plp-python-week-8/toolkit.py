"""My Mini Toolkit - Week 8 project.

A menu-driven program with four small tools:
number guessing game, to-do list, simple calculator and countdown.
"""

import random


# TOOL 1: Number Guessing Game
# The computer picks a number from 1 to 10. The player has 5 tries.
# Uses: a for loop (the attempts), conditionals (too high / too low / correct)
def guessing_game():
    secret = random.randint(1, 10)
    max_tries = 5
    print("\n--- Number Guessing Game ---")
    print(f"I'm thinking of a number from 1 to 10. You have {max_tries} tries!")

    for attempt in range(1, max_tries + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_tries} - your guess: "))
        except ValueError:
            print("That's not a whole number, so you lose this try. Be careful!")
            continue

        if guess == secret:
            print(f"🎉 Correct! The number was {secret}. You got it in {attempt} tries!")
            return
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Out of tries! The secret number was {secret}. Better luck next time!")


# TOOL 2: To-Do List
# Lets the player add, view and complete tasks.
# Uses: a list that changes while the program runs (append / pop),
# a while loop for its own mini menu, and conditionals.
def todo_list():
    tasks = []  # starts empty and changes as the player uses the tool
    print("\n--- To-Do List ---")

    while True:
        print("\n1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as done")
        print("4. Back to main menu")
        choice = input("What would you like to do? (1-4): ").strip()

        if choice == "1":
            task = input("Type your new task: ").strip()
            if task == "":
                print("A task can't be empty. Nothing was added.")
            else:
                tasks.append(task)
                print(f'Added "{task}". You now have {len(tasks)} task(s).')
        elif choice == "2":
            if len(tasks) == 0:
                print("Your list is empty - enjoy the free time! 😎")
            else:
                print(f"You have {len(tasks)} task(s):")
                for number, task in enumerate(tasks, start=1):
                    print(f"  {number}. {task}")
        elif choice == "3":
            if len(tasks) == 0:
                print("There is nothing to complete yet. Add a task first!")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"  {number}. {task}")
                try:
                    number = int(input("Which task number is done? "))
                except ValueError:
                    print("Please type a number.")
                    continue
                if 1 <= number <= len(tasks):
                    finished = tasks.pop(number - 1)
                    print(f'Well done! "{finished}" is complete. {len(tasks)} left.')
                else:
                    print(f"There is no task number {number}.")
        elif choice == "4":
            print("Leaving the to-do list. (Tasks are cleared when you leave.)")
            return
        else:
            print(f'"{choice}" is not an option here. Please choose 1 to 4.')


# TOOL 3: Simple Calculator
# Takes two numbers and an operator, then prints the answer.
# Uses: if / elif / else for the operator and a check for dividing by zero.
def calculator():
    print("\n--- Simple Calculator ---")
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
    except ValueError:
        print("Those weren't both numbers. Returning to the menu.")
        return

    operator = input("Operator (+, -, *, /): ").strip()

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("You can't divide by zero! Try again with a different number.")
            return
        result = first / second
    else:
        print(f'"{operator}" is not a supported operator.')
        return

    print(f"{first} {operator} {second} = {result}")


# TOOL 4: Countdown
# Counts down from a number the player chooses to zero.
# Uses: a for loop with range() counting backwards, and a conditional.
def countdown():
    print("\n--- Countdown ---")
    try:
        start = int(input("Count down from which number? "))
    except ValueError:
        print("Please enter a whole number next time. Returning to the menu.")
        return

    if start < 1:
        print("Pick a number of 1 or more so there is something to count!")
        return

    for number in range(start, 0, -1):
        print(f"{number}...")
    print("Lift off! 🚀")


# MAIN MENU
# Shows the menu again and again until the player chooses Quit (5).
# Uses: a while loop and if / elif / else to run the chosen tool.
def main():
    print("=== Welcome to My Mini Toolkit! ===")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Countdown")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            guessing_game()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            calculator()
        elif choice == "4":
            countdown()
        elif choice == "5":
            print("\nThanks for using My Mini Toolkit. See you next time!")
            break
        else:
            print(f'Oops! "{choice}" is not on the menu. Please pick a number from 1 to 5.')


main()