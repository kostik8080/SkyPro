"""
У вас есть текст в котором встречаются #хештеги

Напишите функцию `get_hash(text)`

Верните все хештеги одним списком

Например:

`get_hash("Котята #еда #закат море")` вернет [”#еда”, “#закат”]

`get_hash("Котята море")` вернет []

Подсказка: Разбейте текст на слова, затем проверьте не решетка ли первый символ
"""
def get_hashtags(text):
    hashtags = []
    for element in text.split(" "):
        if element.startswith("#"):
            hashtags.append(element[1:])

    return hashtags


words = input()
result = get_hashtags(words)
print(" ".join(result))