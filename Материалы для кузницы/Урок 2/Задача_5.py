"""Программа предлагает ввести пользователю год своего рождения
и на основе текущего года (2023) считает его возраст в таком формате:

Вам от 22 до 23
"""

year = int(input("Введите год вашего рождения: "))
current_year = 2023
age = (current_year - year)

if age < 1:
    print(f"Вам {age} лет.")
elif age == 1:
    print("Вам 1 год.")
else:
    pass
if age >= 2:
    print(f"{age - 1} год(а).")
else:
    pass
if age == 2:
    print("Вам 2 года.")
else:
    pass
if age >= 3:
    print(f"{age} года(ов).")
else:
    pass
if age == 3:
    print("Вам 3 года.")
else:
    pass

if age <= 4:
    print(f"{age + 1} года(лет).")
else:
    pass