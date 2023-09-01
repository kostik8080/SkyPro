"""
# Спрашивайте у пользователя (с помощью input() ) ввод пока он не введет "хватит"
# и записывайте каждое полученное значение в список shopping_list
# Когда пользователь набрал "хватит", выведите список, например:

Яблочки
Сыр
Бумага для принтера
"""

shopping_list = []

while True:
    user_string = input("Введите слово: ")
    if user_string in "хватит":
        print(shopping_list)
        break
    else:
        shopping_list.append(user_string)