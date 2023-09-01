"""
Напишите функцию get_grade(grade), которая принимает целое число от 2 до 5 и возвращает оценку

Плохо
Удовлетворительно
Хорошо
Отлично
"""

def get_grade(grade):
    match grade:
        case 2:
            return "Плохо"
        case 3:
            return "Удовлетворительно"
        case 4:
            return "Хорошо"
        case 5:
            return "Отлично"

total = get_grade(3)
print(total)