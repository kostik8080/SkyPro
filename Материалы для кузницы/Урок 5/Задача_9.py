"""
Напишите функцию `has_rrr(word)`, которая проверяет картавость слова, а возвращает булево значение.

Например `has_rrr(”речка”)` вернет True

Например `has_rrr(”уточка”)` вернет False
"""

def has_rrr(word):
    return 'р' in word

print(has_rrr('речка')) # True
print(has_rrr('уточка')) # False