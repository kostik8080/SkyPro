"""Вывести список из 8 степеней числа 2

a = 2

# пример ответа

1 2 4 8 16 32 64 12"""

a = 2

degres = []

for i in range(1, 9):
    degres.append(a ** i)
print(degres)

