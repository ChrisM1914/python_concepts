"""
presidents_list.py
Displays the first ten US Presidents and their terms.
Prints the list twice: once with a for loop and once with a while loop.
Adds an asterisk (*) next to any president whose last name starts with "A".
"""

presidents = [
    ("George Washington", "1789-1797"),
    ("John Adams", "1797-1801"),
    ("Thomas Jefferson", "1801-1809"),
    ("James Madison", "1809-1817"),
    ("James Monroe", "1817-1825"),
    ("John Quincy Adams", "1825-1829"),
    ("Andrew Jackson", "1829-1837"),
    ("Martin Van Buren", "1837-1841"),
    ("William Henry Harrison", "1841-1841"),
    ("John Tyler", "1841-1845"),
]


def display_name(name):
    """Return the name, with an asterisk if the last name starts with A."""
    last_name = name.split()[-1]
    if last_name.startswith("A"):
        return name + " *"
    else:
        return name


print("--- Using a for loop ---")
for name, term in presidents:
    print(f"{display_name(name)} ({term})")

print("\n--- Using a while loop ---")
i = 0
while i < len(presidents):
    name, term = presidents[i]
    print(f"{display_name(name)} ({term})")
    i += 1

print("\n* = last name starts with A")