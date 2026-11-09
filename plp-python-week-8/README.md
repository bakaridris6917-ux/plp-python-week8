# My Mini Toolkit (PLP Python Week 8)

## What it does

My Mini Toolkit is a menu-driven Python program with four small tools. The menu comes back after every tool until you choose Quit, and a wrong choice gets a polite message instead of a crash.

1. **Number Guessing Game** - guess a secret number from 1 to 10 in 5 tries, with "too high" / "too low" hints.
2. **To-Do List** - add tasks, view them and mark them done; the list grows and shrinks while the program runs.
3. **Simple Calculator** - add, subtract, multiply or divide two numbers (it refuses to divide by zero).
4. **Countdown** - counts down from any number to zero, then says "Lift off!".

Concepts used: `while` and `for` loops, `if` / `elif` / `else`, a changing list (`append` / `pop`), f-strings, `try` / `except`, and the `random` module.

## How to run it

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```
python toolkit.py
```

(On some computers use `python3 toolkit.py`.) Type a number from the menu and press Enter.

## Files

- `toolkit_plan.txt` - my plan, written before I built anything
- `toolkit.py` - the program
- `screenshots/` - the menu with an invalid choice, and each tool running
- `README.md` - this file

## Reflection

The hardest part was keeping the program organised: I had to decide how the main menu loop, the to-do list's own mini menu and the other tools would fit together without getting tangled. The bug that took longest to fix was crashes from bad input, because typing letters where the program expected a number made `int()` fail, so I wrapped those inputs in `try` / `except` and added friendly messages. The to-do list was also tricky, since I had to check that a task number was valid before removing it so the list never caused an index error. Writing `toolkit_plan.txt` first really helped, because I already knew the menu text and which concepts each tool needed when I started coding. Testing every menu path, including Quit, showed me small things like what happens when you press Enter on an empty choice. With one more week, I would save the to-do list to a file so my tasks are still there the next time I open the program. I would also add a score tracker and a difficulty setting to the guessing game.
