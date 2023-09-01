"""
Напишите функцию `get_min_sec(sec)` которая принимает время в секундах, возвращает словарь в формате `{”min”: мин, “sec”: сек)}`. Минуты и секунды  целые числа.

Пример `get_min_sec(120)` Вернет `{”min”:2, “sec”:0}`

Пример `get_min_sec(150)` Вернет `{”min”:2, “sec”:30}`

Пример `get_min_sec(15)` Вернет `{”min”:, “sec”:15}`

Подсказка: деление нацело x//y , остаток от деления: x%y
"""

def get_min_sec(sec):
    sec_only = sec % 60
    min_only = sec // 60
    return {"min": min_only, "sec": sec_only}

value = int(input("Введите количество секунд"))
result = get_min_sec(value)
print(result)