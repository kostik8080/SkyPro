"""Программа запрашивает у пользователя номер дня и определяет, может ли быть в месяце такое число.

Если число от 1 до 28 программа выводит:

```python
Такое количество дней в месяце точно есть
```

Если от 29 до 31 :

```python
Такое количество дней в месяце возможно есть
```

Иначе:

Такого количества в месяце точно нет"""

deys_number = int(input("Введите номер дня: "))

if 1 <= deys_number <= 28:
    print("Такое количество дней в месяце точно есть")
elif 29 <= deys_number <= 31:
    print("Такое количество дней в месяце возможно есть")
else:
    print("Такого количества в месяце точно нет")