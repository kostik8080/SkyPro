"""
# Спрашивайте у пользователя список его трат, пока он не введет "хватит"
# и записывайте в список expenses
# Когда пользователь набрал "хватит", выведите список, например:

> 50

"""

express = []

while True:
    user_string = input("Введите список сколько потратили: ")
    if user_string in "хватит":
        print(express)
        break
    else:
        express.append(int(user_string))

