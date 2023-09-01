"""Пользователь вводит два целых числа.

Заполните список четными числами, которые есть в промежутке.

Оба числе не входят в промежуток

Ввод
1
5

Вывод
2
4


Ввод
5
10

Вывод
6
8
"""
user_int_1 = int(input("Введите целое число 1: "))
user_int_2 = int(input("Введите целое число 2: "))

new_letters = []
for num in range(user_int_1, user_int_2):
    if num % 2 == 0:
        new_letters.append(num)

for i in new_letters:
    print(i)