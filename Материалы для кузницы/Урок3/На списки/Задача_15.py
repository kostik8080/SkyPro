"""Пользователь вводит с клавиатуры число, например 65. Программа подтверждает

```python
Вы ввели ___
Осталось ___ до 100.
```

Программа запускает цикл, в каждой итерации предлагая пользователю ввести новое число и дополнить число введенное изначально, пока не будет достигнуто значение 100.

После каждого ввода программа выводит

```python
Вы ввели ___
Осталось __ до 100!
```

В конце программа выводит

Вот и все!
"""
count = 0

while count < 100:
    number_input = int(input("Введите число: "))
    count += number_input
    print(f"Вы ввели {number_input} Осталось {100 - count} до 100")

print()

print("Вот и всё")
