"""
Напишите функцию print_square(x,y) , которая печатает прямоугольник со сторонами X, Y

# Если x = 4, y=2

****
****

# Если x = 4, y=4

****
****
****
****
"""

def print_square(x, y):
    for i in range(y):
        print("*" * x)

x = int(input())
y = int(input())

print_square(x, y)
