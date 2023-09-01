"""
Напишите функцию get_grade(x), которая принимает целочисленные баллы (0-100) и возвращает

0-40 Плохо
41-60 Удовлетворительно
61-80 Хорошо
81-100 Отлично
"""

def get_grade(x):
    if 0 <= x <= 40:
        return "Плохо"
    elif 41 <= x <= 60:
        return "Удовлетворительно"
    elif 61 <= x <= 80:
        return "Хорошо"
    elif 81 <= x <= 100:
        return "Отлично"


balls_int = int(input("Введите число балла: "))
result = get_grade(balls_int)
print(result)