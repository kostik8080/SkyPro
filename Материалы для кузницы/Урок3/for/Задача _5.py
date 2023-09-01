"""Средний возраст взрослых
# В доме живут жители от 0 до 99 лет, вычислите средний возраст тех,
# кому есть 18

residents = [5, 3, 2, 20, 5, 30, 5, 40, 17]

# Пример ответа:
30
"""

residents = [5, 3, 2, 20, 5, 30, 5, 40, 17]

total = []

for i in residents:
    if i >= 18:
        total.append(i)
result = sum(total) / len(total)
print(round(result))