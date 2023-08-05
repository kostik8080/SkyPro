"""
Запустите цикл по индексам дня недели (for i in range), каждую итерацию цикла доставайте элемент с индексом i из
первого, второго, третьего списка (имясписка[i]).

Чтобы получить информацию, рабочий ли день, напишите условие if и превратите булево значение (true/false) в строку
"рабочий/выходной". Затем выведите полученные строки с помощью f-строки.
"""
"""weekdays = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
work = [True, True, True, True, True, False, False]
plans = ["за покупками", "отдыхать", "играть", "лениться", "гулять", "кутить", "страдать"]


for i in range(len(weekdays)):

  if work[i] == True:
    type_of_day = 'рабочий день'
  else:
    type_of_day = 'выходной день'

  print(f'{weekdays[i]} - это {type_of_day}, а вечером {plans[i]}.')


items = [1, 2, 3]

items_plus = [item +1 for item in items]
print(items_plus)"""

# line = input()


"""text = "734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5"
just_words = []
words = text.split()




for ne_spisok_a_slovo in words:
    if ne_spisok_a_slovo.isalpha():
        just_words.append(ne_spisok_a_slovo)  # Список, он же лист - не переменная. += не прокатит. Нужен append()
    else:
        continue
text_cleaned = " ".join(just_words)
print(text_cleaned)"""

# s = "420"
# t = "а"
# r = "@"

# s.isdigit()
# t.isdigit()
# r.isdigit()

# s.isalpha()
# t.isalpha()
# r.isalpha()

# str.isdigit() # проверяет, является ли строка числом
# print(s)
# print(t)
# print(r)


# str.isalpha()  #проверяет, является ли строка нобором букв

students = {
  "Алиса": 70,
  "Эльдар": 20,
  "Агата": 40,
  "Ярослав": 84,
}

user_input = input()

if students[user_input] >= 81:
  print(f"{students[user_input]} баллов, оценка А")
elif 61 <= students[user_input] <= 80:
  print(f"{students[user_input]} баллов, оценка В")
else:
  print(f"{students[user_input]} баллов, оценка С")
