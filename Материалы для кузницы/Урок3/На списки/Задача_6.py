"""у вас есть список слов. Запишите в новый список длину каждого слова, выведите список. Длину слова можно получить с помощью len(слово)

```python
words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
```

Пример списка:

[5,5,7,5,4,7]
"""

words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]

new_word = []

for i in words:
    new_word.append(len(i))

print(new_word)