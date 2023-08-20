"""У вас есть список слов

```python
letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
```

Выведите в отдельном списке четные и отдельно нечетные элементы

Нечетные

Alpha
Charlie
Charlie

Четные

Bravo
Delta
Foxtrot
"""
even_numbers = [] # Чётные
not_even = [] # нечетные

letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]

for letter in range(len(letters)):
    if letter % 2 == 0:
        even_numbers.append(letters[letter])


    elif letter % 2 == 1:
        not_even.append(letters[letter])
print("Нечетные")
print()
for num in even_numbers:
    print(num)
print()

print("Четные")
print()
for num_2 in not_even:
    print(num_2)



