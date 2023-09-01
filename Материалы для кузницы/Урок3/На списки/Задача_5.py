"""Есть два списка.

```python
numbers_1 = [1, 2, 3, 4, 5, 6, 7]
numbers_2 = [8, 9, 10, 11, 12]
```

Вычислите среднее в каждом списке (среднее это сумма деленная на количество).

Выведите

Первое среднее больше
или
Второе среднее больше
или
Средние одинаковые
"""

numbers_1 = [1, 2, 3, 4, 5, 6, 7]
numbers_2 = [8, 9, 10, 11, 12]

result_1 = sum(numbers_1) / len(numbers_1)
result_2 = sum(numbers_2) / len(numbers_2)

if result_1 > result_2:
    print("Первое среднее больше")
elif result_1 < result_2:
    print("Второе среднее больше")
elif result_1 == result_2:
    print("Средние одинаковые")

