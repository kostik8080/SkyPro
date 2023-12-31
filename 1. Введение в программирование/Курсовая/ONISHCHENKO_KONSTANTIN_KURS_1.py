# Функция рандом
import random

# Список правивильных и неправильных ответов True/False
answers = []

# Список английских слов
words_angl = ["multicoloured", "try", "creative", "difference", "sos"]

# Словарь английских слов и символов и кодировка азбуки морзе
morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "я": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

input("Сегодня мы потренируемся расшифровывать морзянку.Нажмите Enter и начнем")


def morse_encode(words):
    """
    Функция которая переводит все символы и
    английские буквы в кодировку
    азбуки морзе
    """
    encoding_list = []
    for word in words:
        for value in morse:
            if value == word.lower():
                encoding_list.append(morse[value])
    encoding_string = " ".join(encoding_list)
    return encoding_string


# print(morse_encode("sos"))


def get_word():
    """
     Функция рандомно
     выводит английское слово
     из списка
    """
    global word_random
    word_random = random.choice(words_angl)
    return word_random


# Цикл задает 5 вопросов в кодировке морзе и проверяет верно ответил или нет
for questions in range(len(words_angl)):
    print(f"Слово {questions + 1} -  {morse_encode(get_word())}")
    answer_i = (input())
    if answer_i == word_random:
        print(f"Верно, {word_random}!")
        answers.append(True)
    else:
        print(f"Неверно, {word_random}!")
        answers.append(False)


def statistics(answers):
    """
    Статистика сколько вопросов было,
    Сколько было правельных ответов,
    Сколько ответил не провильно
    """

    number_of_correct = answers.count(True)
    number_of_incorrect = answers.count(False)
    print(f"Всего задачек: {questions + 1}")
    print(f"Отвечено верно: {number_of_correct}")
    print(f"Отвечено неверно: {number_of_incorrect}")


statistics(answers)
