"""У вас есть список из чисел.

Соберите список позиций (индексов) на которых расположены 0 и 1



```python
numbers = [7,62,1,3,1,2,0,1]
```

Пример вывода:

[2, 4, 6, 7]
"""
numbers = [7,62,1,3,1,2,0,1]

new_numbers = []

for num in range(len(numbers)):
    if numbers[num] == 0:
        new_numbers.append(num)
    elif numbers[num] == 1:
        new_numbers.append(num)
print(new_numbers)