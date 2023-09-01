"""
Напишите функцию, которая получит строку и вернет статистику в виде словаря с ключами:

`wordcount` – количество слов

`symbolcount` – количество символов

`spacecount` – количество пробелов

def get_string_stats(string):
    pass


print(get_string_stats("Кот это не хлеб"))

# Вернет {"wordcount": 4, "symbolcount": 15, "spacecount": 3}
"""


def get_string_stats(string):
    wordcount = string.split(" ")
    symbolcount = string.strip()
    spacecount = string.count(" ")

    return {"wordcount": len(wordcount), "symbolcount": len(symbolcount), "spacecount": spacecount}


print(get_string_stats("Кот это не хлеб"))

# Вернет {"wordcount": 4, "symbolcount": 15, "spacecount": 3}