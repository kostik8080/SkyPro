# Объявляем переменные
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

difficulty_level = {
    "легкий": words_easy,
    "средний": words_medium,
    "тяжелый": words_hard,
}

answers = {}
rang_levels = 0

# Выбираем сложность
hard = input("Выберите уровень сложности: (Лёгкий  Средний  Сложный) : ")

# Запускаем цикл - вопрос / ответ
worc_dic = difficulty_level[hard]
for key, value in worc_dic.items():
    answer = input(f"{key}, {len(value)} букв, начинается на {value[0]}... Ответ: ")
    if answer == value:
        print(f"Верно {key} - это {value}")
    else:
        print(f"не верно {key} - это {value}")
    answers[key] = answer == value

# Выводим статистику правильных и не правильных ответов
print()
print("Правильно отвеченные слова")
for word, bool_value in answers.items():
    if bool_value is True:
        print(word)
        rang_levels += 1

print()
print("Неправильно отвеченные слова")
for word, bool_value in answers.items():
    if bool_value is False:
        print(word)

# Подсчет ранга
print(f"Ваш ранг: \n{levels[rang_levels]}")
