"""
# Инверсия
# С помощью цикла выведите список в обратном порядке

letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]

Пример ответа:

# Foxtrot Echo Delta Charlie Bravo Alpha
"""

letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]

for i in letters[::-1]:
    print(i)