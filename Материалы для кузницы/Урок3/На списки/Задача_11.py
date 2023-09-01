"""У нас есть список из элементов.
Соберите список позиций (индексов) на которых расположены числа.

Для проверки используй метод строки `.isdigit()`

```python
items = ["0", "1", "resist", "2", "tower", "3", "alpha", "4"]
```

Пример вывода:

[0, 1, 3, 5, 7]
"""
new_items = []

items = ["0", "1", "resist", "2", "tower", "3", "alpha", "4"]

for num in range(len(items)):
    if items[num].isdigit():
        new_items.append(num)
print(new_items)