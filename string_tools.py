"""
string_tools.py
Prompts the user for a sentence and demonstrates string manipulation.
Transformations: reverse, uppercase, title case, formatted output.
Analysis: word count, substring occurrence count, palindrome detection.
Input is stripped and must be between 5 and 200 characters.
"""

MIN_LEN = 5
MAX_LEN = 200


def get_text(prompt):
    """Keep asking until the user enters text within the length limits."""
    while True:
        text = input(prompt).strip()
        if MIN_LEN <= len(text) <= MAX_LEN:
            return text
        print(f"Please enter between {MIN_LEN} and {MAX_LEN} characters.")


def get_nonempty(prompt):
    """Keep asking until the user enters something non-empty."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty.")


text = get_text("Enter a sentence: ")

# --- Transformation ---
print("\n--- Transformations ---")
print("Reversed:  ", text[::-1])
print("Uppercase: ", text.upper())
print("Title case:", text.title())

# --- Analysis ---
cleaned = text.replace(";", "").replace(".", "").replace(",", "").lower()
words = cleaned.split()
palindromes = [w for w in words if len(w) > 1 and w == w[::-1]]

search = get_nonempty("\nEnter a substring to count: ").lower()

print("\n--- Analysis ---")
print(f"Word count: {len(words)}")
print(f"First 4 words: {words[:4]}")
print(f"'{search}' appears {text.lower().count(search)} time(s)")
print(f"Palindromes found: {palindromes if palindromes else 'none'}")
print(f"\nSummary: {len(words)} words, {len(palindromes)} palindrome(s).")