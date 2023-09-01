"""
Напишите функцию, которая получит список строк, а вернет список их первых букв:

def get_first_letters(strings):
		pass


print(get_first_letters(["Alpha", "Bravo", "Charlie"])) # >>  ["A","B","C"]
"""

def get_first_letters(strings):
    word_list = []
    for letter in strings:
        word_list.append(letter[0])
    return word_list

result = get_first_letters(["Alpha", "Bravo", "Charlie"])
print(result)