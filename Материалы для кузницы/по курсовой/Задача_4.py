"""
Напишите функцию, которая проверяет, все ли элементы в списке начинаются с “а”

def check_if_a_is_first(strings):
		pass


print(check_if_a_is_first(["a"]))  # вернет True
print(check_if_a_is_first(["a", "Aaa", "aloha"]))  # вернет True
print(check_if_a_is_first(["a", "boo", "aloha"]))  # вернет False
print(check_if_a_is_first(["b", "c", "d"]))  # вернет False
"""

def check_first_char(s):
    return s[0] == "a"

def check_if_a_is_first(lst):
    for i in range(len(lst)):
        if not check_first_char(lst[i]):
            return False
        else:
            return True

result = check_if_a_is_first(["b", "A", "d"])
print(result)