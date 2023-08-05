# 2 Списка, 1й с вопросами, 2й с правильнами ответами
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# Счетчик правильных ответов
CORRECT_ANSWERS = 0
SCORE = 0

# Знакомимся с ползователем
user_name = input("Введите свое имя!: ").title()
# print(f"Привет, {user_name}")

print(f"Привет! {user_name} Предлагаю проверить свои знания английского!\nНаберите 'ready', чтобы начать!: ")
user_ready = input()
if user_ready.lower() == "ready":
    pass

    # Задаем 1 вопрос
    for i in range(len(questions)):
        if questions[i] == "My name ___  Vova":
            print("My name ___ Vova.")
            answer_1 = input()
            while True:

                if answer_1.lower() == answers[i]:
                    print(f"Ответ верный\nВы получаете {SCORE} баллов!\n")
                    CORRECT_ANSWERS += 1
                    break
                    answer_1 = input()
                if answer_1.lower() != answers[i]:
                    print("Осталось попыток: 2, попробуйте еще раз!\n")
                    CORRECT_ANSWERS += 1
                    answer_1 = input()
                    if answer_1.lower() != answers[i]:
                        print("Осталось попыток: 1, попробуйте еще раз!\n")
                        CORRECT_ANSWERS += 1
                        answer_1 = input()
                    if answer_1.lower() != answers[i]:
                        print(f"Неправильно.\nПравильный ответ: {answers[i]}\n")
                        CORRECT_ANSWERS += 1
                        break

    # Задаем 2 вопрос
    for i in range(len(questions)):
        if questions[i] == "I ___ a coder":
            print("I ___ a coder.")
            answer_2 = input()
            while True:

                if answer_2.lower() == answers[i]:
                    print(f"Ответ верный\nВы получаете {SCORE} баллов!\n")
                    CORRECT_ANSWERS += 1
                    break
                    answer_2 = input()
                if answer_2.lower() != answers[i]:
                    print("Осталось попыток: 2, попробуйте еще раз!\n")
                    CORRECT_ANSWERS += 1
                    answer_2 = input()
                    if answer_2.lower() != answers[i]:
                        print("Осталось попыток: 1, попробуйте еще раз!\n")
                        CORRECT_ANSWERS += 1
                        answer_2 = input()
                    if answer_2.lower() != answers[i]:
                        print(f"Неправильно.\nПравильный ответ: {answers[i]}\n")
                        CORRECT_ANSWERS += 1
                        break

    # Задаем 3 вопрос
    for i in range(len(questions)):
        if questions[i] == "I live ___ Moscow":
            print("I live ___ Moscow")
            answer_3 = input()
            while True:

                if answer_1.lower() == answers[i]:
                    print("Ответ верный\nВы получаете 10 баллов!\n")
                    CORRECT_ANSWERS += 1
                    SCORE += 3
                    break
                    answer_1 = input()
                if answer_1.lower() != answers[i]:
                    print("Осталось попыток: 2, попробуйте еще раз!\n")
                    CORRECT_ANSWERS += 1
                    SCORE += 2

                    answer_1 = input()
                    if answer_1.lower() != answers[i]:
                        print("Осталось попыток: 1, попробуйте еще раз!\n")
                        CORRECT_ANSWERS += 1
                        SCORE += 1

                        answer_1 = input()
                    if answer_1.lower() != answers[i]:
                        print(f"Неправильно.\nПравильный ответ: {answers[i]}\n")
                        CORRECT_ANSWERS += 1
                        SCORE += 1
                        break

    # Расщет процентов
    percent = CORRECT_ANSWERS / 3 * 100
    percent_round = round(percent, 2)

    # Выводим результат и прощальное смс
    print(
        f"Вот и всё, {user_name} \nВы ответили на {CORRECT_ANSWERS} вопросов из 3 верно.\nВы заработали {SCORE} баллов. Это {percent_round} процентов.")

else:
    print("Кажется, вы не хотите играть. Очень жаль.")
