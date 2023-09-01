"""
У вас есть строка.

```python
line = "abcdefghijklmnopqrstuvwxyz"
```

Со стандартного ввода одной строкой подаются два числа x и y, разделенные дефисом.

```python
1-4
```

Разделите строку с помощью split и верните буквы в соответствующем интервале (от x до y) ВКЛЮЧИТЕЛЬНО. Пример вывода

bcde
"""
letter_list = []
line = "abcdefghijklmnopqrstuvwxyz"


number = input("Введите интервал чисел")

line_one = number.split("-")
for num in line_one:
    num_int = int(num)
    #print(num_int)
    letter_list.append(num_int)

print(line[letter_list[0]:letter_list[1]+1])
