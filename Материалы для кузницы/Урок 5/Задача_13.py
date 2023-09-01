"""
Напишите функцию `get_discount(summ)` которая возвращает уровень скидки или бонусной карты в
зависимости от суммы покупок. Уровень – это целое число! Правила вычисления уровня:

1 до 5000

2 до 10000

3 до 20000

4 до 35000

5 до 50000

6 от 50000 и выше

Например `get_discount(7000)` возвращает 2
"""

def get_discount(summ):
    if summ < 5000:
        return 1
    elif summ < 10000:
        return 2
    elif summ < 20000:
        return 3
    elif summ < 35000:
        return 4
    elif summ < 50000:
        return 5
    elif summ >= 50000:
        return 6
summ = int(input("Введите сумму: "))
result = get_discount(summ)
print(result)