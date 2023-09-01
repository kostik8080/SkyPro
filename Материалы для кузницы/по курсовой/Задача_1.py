"""
**Задание 1 - подсчет количества**

Напишите функцию, которая получала бы список булек и возвращала бы количество True в полученном списке.
def count_for_true(elements):
    pass


print(count_for_true([True, True, True]))  # вернет 3
print(count_for_true([False, True, False]))  # вернет 1
"""

def count_for_true(elements):
    summ_true = elements.count(True)
    summ_false = elements.count(False)
    return summ_true

result = count_for_true([False, True, False])
print(result)