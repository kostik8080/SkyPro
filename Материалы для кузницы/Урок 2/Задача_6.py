"""Пользователь вводит вес некоторого предмета в пудах (все значения целые), программа должна сделать вывод  в килограммах в формате:

1 пуд – это примерно 16 килограмм

2 пуда это 32 килограмм
"""

num_in_pudov = int(input("Введите вес в пудах: "))

one_pud = 16

total = num_in_pudov * one_pud
print(f"{num_in_pudov} пуда это {total} килограмм")