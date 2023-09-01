"""У вас есть список гласных.

Запишите в новый список встреченные согласные.

```python
letters = ["A", "B", "I", "O", "Q", "Z"]

vowels = ["A", "E", "I", "O", "U", "Y"]
```

Пример списка:

["B", "Q", "Z"]
"""

new_letters = []
letters = ["A", "B", "I", "O", "Q", "Z"]

vowels = ["A", "E", "I", "O", "U", "Y"]

for i in letters:
    if i not in vowels:
        new_letters.append(i)
print(new_letters)