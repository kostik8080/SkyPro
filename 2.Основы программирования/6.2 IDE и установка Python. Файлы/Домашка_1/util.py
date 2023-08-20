import random

user_name = input("Введите ваше имя: ")
letters_list = []

def reading_words(filename):
    lines = ""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for word in file:
            letters = word.strip("\n").split(" ")
            letter_join = "".join(letters)
            #letters_list.append(letter_join)
            return letter_join
word_string = reading_words()
print(word_string)


def get_random():
    global word_random
    word_random = "".join(random.sample(word_string, len(word_string)))
    return word_random

# print(get_random())
random_text = get_random()
#
#
for questions in word_string:
    print(f"Угадайте слово  -  {random_text}")
    answer_i = (input())
    if answer_i in word_string:
        print(f"Верно, {word_string}!")
        #answers.append(True)
    else:
        print(f"Неверно, {word_string}!")
        #answers.append(False)
print(letters_list)