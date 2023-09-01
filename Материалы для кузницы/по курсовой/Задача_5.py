"""
Напишите функцию, которая создаст два случайных числа 1-100 и вернет их в виде списка

def get_two_randoms():
		...
    return [ , ]


print(get_two_randoms())
"""
import random

def get_two_randoms():
    letters = []
    random_number1 = random.randint(1,100)
    random_number2 = random.randint(1,100)
    letters.append(random_number1)
    letters.append(random_number2)

    return letters


print(get_two_randoms())