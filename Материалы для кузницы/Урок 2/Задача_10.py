"""Напишите код который получает у пользователя сейчас времени (в часах)

Затем выводит сейчас утро / сейчас ночь / сейчас вечер.

Границы периодов такие:
0-6 ночь
7-11 утро
12-17 день
18-24 - вечер
"""

hours_time = int(input("Введите время в часах: "))

if 0 <= hours_time <= 6:
    print("сейчас ночь")
elif 7 <= hours_time <= 11:
    print("сейчас утро")
elif 12 <= hours_time <= 17:
    print("сейчас день")
elif 18 <= hours_time <= 24:
    print("сейчас вечер")
else:
    print("я не знаю что вы ввели")