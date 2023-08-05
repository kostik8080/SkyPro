
# 2 Списка, 1й с вопросами, 2й с правильнами ответами
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# Счетчик правильных ответов
CORRECT_ANSWERS = 0

# Знакомимся с ползователем
user_name = input("Введите свое имя!: ").title()
#print(f"Привет, {user_name}")

print(f"Привет! {user_name} Предлагаю проверить свои знания английского!\nНаберите 'ready', чтобы начать!: ")
user_ready = input()
if user_ready.lower() == "ready":
    pass

    # Задаем 1 вопрос
    for i in range(len(questions)):
        if questions[i] == "My name ___  Vova":
            print("My name ___ Vova.")
            answer_1 = input()
            if answer_1.lower() == answers[i]:
                print("Ответ верный\nВы получаете 10 баллов!\n")
                CORRECT_ANSWERS += 1
            else:
                print(f"Неправильно.\nПравильный ответ: {answers[i]}\n")

                # Задаем 2 вопрос
            for i in range(len(questions)):
                if questions[i] == "I ___ a coder":
                    print("I ___ a coder.")
                    answer_2 = input()
                    if answer_2.lower() == answers[i]:
                        print("Ответ верный\nВы получаете 10 баллов!\n")
                        CORRECT_ANSWERS += 1
                    else:
                        print(f"Неправильно.\nПравильный ответ: {answers[i]}\n")

                # Задаем 3 вопрос
            for i in range(len(questions)):
                if questions[i] == "I live ___ Moscow":
                    print("I live ___ Moscow")
                    answer_3 = input()
                    if answer_3.lower() == answers[i]:
                        print("Ответ верный\nВы получаете 10 баллов!\n")
                        CORRECT_ANSWERS += 1
                    else:
                        print(f"Неправильно.\nПравильный ответ: {answers[i]}\n")

    #Расщет процентов
    percent = CORRECT_ANSWERS / 3 * 100
    percent_round = round(percent, 2)

    #Выводим результат и прощальное смс
    print(f"Вот и всё, {user_name} \nВы ответили на {CORRECT_ANSWERS} вопросов из 3 верно.\nВы заработали {CORRECT_ANSWERS * 10} баллов. Это {percent_round} процентов.")

else:
    print("Кажется, вы не хотите играть. Очень жаль.")
