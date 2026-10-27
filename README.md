# python_concepts
Assignment is to give you practical experience applying Python syntax and semantics to solve simple, real world tasks.

It also provides practice for input validation,
string manipulation, loops, and exception handling.

## How to run
Open a terminal in the repo folder and run any script:

    python presidents_names.py
    python president_lookup.py
    python string_tools.py
    python age_checker.py

## Programs
- [presidents_names.py](presidents_names.py): Prints the first ten presidents and
  their terms using a for loop and a while loop. Last names starting with "A"
  get an asterisk.
- [president_lookup.py](president_lookup.py): Looks up one of the ten presidents
  by number (1-10) using try/except to handle bad input and numbers that are out
  of range.
- [string_tools.py](string_tools.py): Asks for a sentence, then recreates it
  (reverse, uppercase, title case) and analyzes it (word count, substring count, 
  palindrome detection).
- [age_checker.py](age_checker.py): Asks for an age (integer) and a height in
  feet (float), it prompts until both are valid.

## Assumptions
- Number must be between 1-10.
- Year must be 1789-1845; minimum term length must be 0-8 years.
- Sentence must be between 5 - 200 characters.
- Substring must be numerical value.
- Number must be between 0 - 120.
- Height must use (.) between feet and inches.

## Testing and edge cases
- Entered `0` in president_lookup.py and was re-prompted.
- Entered 1 word, 2 characters in string_tools.py and was re-prompted.
- Entered `b` instead of a numerical value and was re-prompted.
