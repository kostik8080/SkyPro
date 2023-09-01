"""
У вас есть текст в котором встречаются хештеги и упоминания .

Напишите функцию `get_hashes_and_mentions(text)`

Функция должна возвращать словарь типа {"hashes": ..., "mentions": ...}

Например:

`get_hashes_and_mentions("Котята #еда @Вася море")`

вернет

{"hashes": [”#еда”], "mentions": [”@Вася”]}
"""
def get_hashes_and_mentions(text):
    hashes = set()
    mentions = set()

    for word in text.split():
        if word.startswith('#'):
            hashes.add(word[:])

        elif word.startswith('@'):
            mentions.add(word[:])

    return {'hashes': list(hashes), 'mentions': list(mentions)}


text = input("Введите слово")
result = get_hashes_and_mentions(text)
print(result)