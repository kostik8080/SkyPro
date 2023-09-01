"""У вас есть список чисел.

```python
numbers = [12, 27, 36, 55, 3, 16, 24, 33, 55]

```

Напишите, сколько чисел нужно просуммировать, чтобы получить сумму 100 или выше

Пример вывода:

Сумма: 130
Чисел: 4
"""


numbers = [12, 27, 36, 55, 3, 16, 24, 33, 55]

sum_of_numbers = 0
count = 0

while sum_of_numbers < 100:
    sum_of_numbers += numbers[count]
    count += 1

print("Сумма:", sum_of_numbers)
print("Чисел:", count)