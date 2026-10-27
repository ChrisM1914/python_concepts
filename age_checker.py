"""
age_checker.py
Prompts for an age (integer) and a height in feet (float).
Re-prompts until valid numbers are entered, then prints a short summary.
Demonstrates input validation with try/except ValueError.
"""

from datetime import date


def get_int(prompt, low, high):
    """Prompt until the user enters a whole number between low and high."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("That is not a whole number. Try again.")
            continue
        if low <= value <= high:
            return value
        print(f"Please enter a number between {low} and {high}.")


def get_float(prompt, low, high):
    """Prompt until the user enters a decimal number between low and high."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("That is not a valid number. Try again.")
            continue
        if low <= value <= high:
            return value
        print(f"Please enter a number between {low} and {high}.")


age = get_int("Enter your age: ", 0, 120)
height = get_float("Enter your height in feet (e.g. 5.9): ", 1.0, 9.0)

birth_year = date.today().year - age
print(f"\nYou are {age} years old (born around {birth_year}).")
print(f"Your height is {height:.1f} ft ({height * 30.48:.0f} cm).")