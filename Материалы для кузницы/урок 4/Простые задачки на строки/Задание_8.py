"""
У вас есть словарь сокращений, выведите слова для которых сокращения составлены неверно c указанием правильных сокращений.

```jsx
words = {"Alpha": "A", "Bravo":"V", "Charlie": "C", "Delta": "D", "Echo": "H"}
```

Пример вывода
B is for Bravo
E is for E
"""

words = {"Alpha": "A", "Bravo":"V", "Charlie": "C", "Delta": "D", "Echo": "H"}

for key, value in words.items():
    if key[0] != value:
        print(f"{key[0]} is for {key}")