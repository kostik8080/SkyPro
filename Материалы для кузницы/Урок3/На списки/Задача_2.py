"""В списке есть несколько чисел.

```python
numbers = [4,5,7,8,10]
```

Пользователь  вводит с клавиатуры два числа. Выведите в зависимости от попадания этих чисел в предоставленный ряд
Оба числа есть
Одно из чисел есть
Ни одного из чисел нет
"""

numbers = [4,5,7,8,10]

user_number_1 = int(input("Введите число: "))
user_number_2 = int(input("Введите число: "))

if user_number_1 in numbers and user_number_2 in numbers:
    print("Оба числа есть")
elif  user_number_1 in numbers or user_number_2 in numbers:
    print("Одно из чисел есть")
else:
    print("Ни одного из чисел нет")