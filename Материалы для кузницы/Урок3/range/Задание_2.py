"""# Вывести список всех чисел меньше 120, в которых присутствует цифра 1


# пример ответа

1 10 11 21 31 41 51 61 71 81 91 100 101 110 111
"""



new_number = []

for i in range(1, 120 +1):
    if str(i).find("1") != -1:
        new_number.append(i)
print(new_number)


