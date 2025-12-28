"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""
def stupidPassword(n: int, l: int):
    passwords = []

    # Generate first l letters of the alphabet
    letters = [chr(ord('a') + i) for i in range(l)]

    # Iterate through all possible combinations
    for d1 in range(1, n + 1):
        for d2 in range(1, n + 1):
            for letter1 in letters:
                for letter2 in letters:
                    # Character 5 must be greater than both d1 and d2
                    max_digit = max(d1, d2)
                    for d5 in range(max_digit + 1, n + 1):
                        password = f"{d1}{d2}{letter1}{letter2}{d5}"
                        passwords.append(password)

    # Passwords are already in alphabetical order due to iteration order
    return passwords



