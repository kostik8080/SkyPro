"""
Напишите функцию `print_square()`, которая печатает квадрат 2 на 4, вот такой

****
****
"""

# def print_square():
#     for row in range(2):
#         return (' '.join([str("*") for x in range(1, 5)]))
# print(print_square())
# print(print_square())

def print_square():
    for x in range(2,5):
        string_num = ' '.join(str("*"))
        return (string_num * x * x) + (f"\n{string_num * x * x}")

print(print_square())