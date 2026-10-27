"""
president_lookup.py
Lets the user look up one of the first ten US Presidents by number (1-10).
Demonstrates exception handling: ValueError for bad input and IndexError
for out-of-range list access, with a retry option.
"""

presidents = [
    "George Washington", "John Adams", "Thomas Jefferson", "James Madison",
    "James Monroe", "John Quincy Adams", "Andrew Jackson", "Martin Van Buren",
    "William Henry Harrison", "John Tyler",
]

while True:
    raw = input("Enter a president number (1-10): ").strip()
    try:
        number = int(raw)
        print(f"President #{number} is {presidents[number - 1]}")
        if number < 1:
            raise IndexError
    except ValueError:
        print("Please enter a whole number, like 4.")
    except IndexError:
        print("That number is out of range. Choose 1 through 10.")

    again = input("Look up another? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break