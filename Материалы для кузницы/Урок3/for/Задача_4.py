"""
# В доме живут жители от 0 до 99 лет, вычислите средний возраст

residents = [5, 3, 2, 20, 5, 30, 5, 40, 17]

# Пример ответа:
15
"""

residents = [5, 3, 2, 20, 5, 30, 5, 40, 17]

total = 0

for i in residents:
    total += i
result = total / len(residents)
print(round(result))