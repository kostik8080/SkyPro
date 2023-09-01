"""
У нас есть словарь покупок. Также есть список ключей словаря.
Удалите указанные ключи, затем выведите сумму значений словаря с оставшимися ключами.
Удалить можно через del … / pop(…)
shopping_list = {
  "bread": 70,
  "milk": 150,
  "cookies": 180,
  "oranges": 220,
  "apples": 120,
}

items_to_remove = ["apples", "milk"]

Пример вывода:

470
"""

shopping_list = {
  "bread": 70,
  "milk": 150,
  "cookies": 180,
  "oranges": 220,
  "apples": 120,
}

items_to_remove = ["apples", "milk"]

for key in items_to_remove:
    del shopping_list[key]
    total_sum = sum(v for k, v in shopping_list.items() if k not in items_to_remove)

print(total_sum)