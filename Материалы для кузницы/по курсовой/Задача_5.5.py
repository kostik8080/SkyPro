"""
У вас есть строка. Напишите функцию, которая вернет три случайные буквы.

letters = "abcdefghijklmnopqrstuvwxyz"

def three_random_letters(letters):
    return ...

print(three_random_letters(letters))

# вернет ["c", "k", "s"]
"""
import random

letters = "abcdefghijklmnopqrstuvwxyz"


def three_random_letters(letters):
    random_letter = random.sample(letters, 3)

    return random_letter

print(three_random_letters(letters))