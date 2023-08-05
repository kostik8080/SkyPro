"""
Запустите цикл по индексам дня недели (for i in range), каждую итерацию цикла доставайте элемент с индексом i из
первого, второго, третьего списка (имясписка[i]).

Чтобы получить информацию, рабочий ли день, напишите условие if и превратите булево значение (true/false) в строку
"рабочий/выходной". Затем выведите полученные строки с помощью f-строки.
"""
weekdays = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
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
print(items_plus)
