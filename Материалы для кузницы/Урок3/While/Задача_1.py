"""
# Спрашивайте сделал ли пользовтель домашку, пока он не скажет да

# Пример ответа:

Ты сделал домашку?
> Нет
Ты сделал домашку?
> Угу
Ты сделал домашку?
> Да
Какой ты молодец"
"""

while True:
    user_string = input("Ты сделал домашку?: ")
    if user_string.lower() in "да":
        print()
        print("Какой ты молодец")
        break

