# Счетчик правильных ответов
CORRECT_ANSWERS = 0

# Знакомимся с ползователем
print("Привет! Предлагаю проверить свои знания английского!\nНапиши, как тебя зовут?")
user_name = input()
print(f"Привет, {user_name}, начинаем тренировку!")
print()
# Задаем 1 вопрос
print("My name ___ Vova.")
answer_1 = input()
if answer_1.lower() == "is":
    print("Ответ верный\nВы получаете 10 баллов!")
    CORRECT_ANSWERS += 1
else:
    print("Неправильно.\nПравильный ответ: is")

print()
# Задаем 2 вопрос
print("I ___ a coder..")
answer_2 = input()
if answer_2.lower() == "am":
    print("Ответ верный\nВы получаете 10 баллов!")
    CORRECT_ANSWERS += 1
else:
    print("Неправильно.\nПравильный ответ: am")

print() # Задаем 3 вопрос
print("I live ___ Moscow.")
answer_3 = input()
if answer_3.lower() == "in":
    print("Ответ верный\nВы получаете 10 баллов!")
    CORRECT_ANSWERS += 1
else:
    print("Неправильно.\nПравильный ответ: in")

print()

# Расщет процентов
percent = CORRECT_ANSWERS / 3 * 100

# Выводим результат и прощальное смс
print(f"Вот и всё, {user_name}!\nВы ответили на {CORRECT_ANSWERS} вопросов из 3 верно.\nВы заработали {CORRECT_ANSWERS * 10} баллов.Это {round(percent, 2)} процентов.")