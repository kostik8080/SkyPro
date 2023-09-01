"""[3, 7, 10, 0, "x", 20, "d", 4, 2]

Если очередной элемент число (type(...) == int)

то

новое число добавляется к сумме уже суммированных.

Если же очередной элемент буква (type(...) == str)

то

x - сумма умножается на 2

d - делится на два

Окргуление ведется вниз до ближайшего целого числа

Пример вывода

36
"""
import math
total = 0

letters = [3, 7, 10, 0, "x", 20, "d", 4, 2]

for num in letters:
    if type(num) == int:
        total += num
    elif type(num) == str:
        var = total * 2 / 2

print(total)
#print(math.floor(var))

#print(math.floor(total))