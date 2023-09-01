"""В программе указан код 1239.

У пользователя есть 3 попытки его угадать.

Программа предлагает пользователю ввести код

Затем читает ввод пользователя

Если код верный – вывести верно

Если код неверный - вывести “неверно” и повторять пока есть попытки

Если попытки закончились – вывести “вход заблокирован”"""

password_num = "1239"
score = 3


while score > 0:
    user_password = input("Введите пароль: ")
    if user_password == password_num:
        print("Верно")
        break
    else:
        if user_password in password_num:
            print("неверно")
            continue
        score -= 1
        print(f"У вас осталось {score} попыток")

if score == 0:
    print("Вход заблокирован")
elif user_password == password_num:
    print("Вход разрешен")