"""
У вас есть список слов.

Есть короткие слова (2-3 буквы) – `short`

Есть средние слова (4-6 букв) – `medium`

Если длинные слова (7+букв) – `long`

```python
words = ["уж", "сыр", "кошка", "номер", "деревня", "радиация"]
```

Создайте словарь, где каждому слову добавляется категория:

{
"уж": "short",
"сыр":"short",
"кошка":"medium",
"номер":"medium",
"деревня":"long",
"радиация":"long",
}
"""

words = ["уж", "сыр", "кошка", "номер", "деревня", "радиация"]

word_dict = {}

for word in words:
    if 1 <= len(word) <= 3:
        word_dict[word] = "shart"
    elif 4 <= len(word) <= 6:
        word_dict[word] = "medium"
    elif 7 <= len(word) <= 10 :
        word_dict[word] = "long"
print(word_dict)