"""# позиции нулей
# Вывести все позиции на которых стоят нули

sequence = [0, 1, 1, 0, 1, 0, 0, 1]

# пример ответа
0
3
5
6"""


sequence = [0, 1, 1, 0, 1, 0, 0, 1]

for i in range(len(sequence)):
    if sequence[i] == 0:
        print(i)