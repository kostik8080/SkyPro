"""
Напишите функцию `get_square(radius)`, которая возвращает площадь кружочка.

Функция принимает радиус кружочка

Площадь кружочка = `радиус ** 2 * Пи`

Пи можно считать равным 3.14 или получить из math.pi (math нужно будет импортировать)
"""

import math

def get_square(radius):
    result = radius ** 2 * math.pi
    return round(result)


print(get_square(5))