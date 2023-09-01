"""
У вас есть список слов в которых есть упоминания типа @cat.
Положите в список только эти слова, но без символа @

def get_mentions(words):
    ....


words = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]

print(get_mentions(words)) # вернет ["кот", "хлеб", "подумай"]
"""


def get_mentions(words):
    hashtags = []
    for letter in words:
        if letter.startswith("@"):
            hashtags.append(letter[1:])
    return hashtags



words = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]

print(get_mentions(words))  # вернет ["кот", "хлеб", "подумай"]