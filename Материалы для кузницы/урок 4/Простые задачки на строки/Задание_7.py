"""
У вас есть список, составьте на его основе словарь с акронимами (первые буквы)

Исходный список:

```jsx
words = ["Alpha", "Charlie"]
```

Пример результата

{"Alpha": "A", "Charlie": "C"}
"""

words = ["Alpha", "Charlie"]

words_dict = {}

for word in words:
    word_d = word[0]
    words_dict[word] = word_d
print(words_dict)
