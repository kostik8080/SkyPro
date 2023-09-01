"""Программа запускает цикл, в котором предлагает пользоваетелю ввести число и суммирует числа.

Если число больше 0 – программа его прибавляет к сумме.

Если число меньше 0 – игнорирует

Если число 0 – прекращает работу и выводит сумму"""

score = 0

while True:
    number_int = int(input("Введите число: "))
    if number_int > 0:
        score += number_int
    elif number_int < 0:
        continue
    elif number_int == 0:
        break
print(score)