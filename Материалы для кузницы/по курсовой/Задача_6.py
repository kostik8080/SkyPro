"""
Напишите функцию, которая получит список и вернет словарь с указанием длины, минимального,
 максимального числа. Испольуйте функции max, min, len

def get_info_from_list(numbers):
    pass
    return {"min": ... , "maх": ... , "len": ...}

print(get_info_from_list([1, 5, 10, 15]))

# вернет {"min": 1, "max": 10, "len": 4}
"""

def get_info_from_list(numbers):
    number_min = min(numbers)
    number_max = max(numbers)
    number_len = len(numbers)

    return {"min": number_min , "maх": number_max , "len": number_len}

print(get_info_from_list([1, 5, 10, 15]))

# вернет {"min": 1, "max": 10, "len": 4}