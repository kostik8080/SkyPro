"""
Напишите функцию the_longest(words), которая возвращает самое длинное слово из списка.
 Например the_longest(["еж" , "вещь", "стриж"]) вернет "стриж"
"""

def the_longest(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
result = the_longest(["еж", "вещь", "стриж"])
print(result)
