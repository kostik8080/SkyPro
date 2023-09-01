"""
Напишите функцию `get_period(hour)` которая принимает целочисленный час суток 0-24 и возвращает

0-6 ночь
7-11 утро
12-17 день
18-24 - вечер
"""

def get_period(hour):
    if 0 <= hour <= 6:
        return "ночь"
    elif 7 <= hour <= 11:
        return "утро"
    elif 12 <= hour <= 17:
        return "день"
    elif 18 <= hour <= 24:
        return "вечер"
    else:
        return "нет такого времени"


hour = int(input("Введите который час: "))

total = get_period(hour)
print(total)