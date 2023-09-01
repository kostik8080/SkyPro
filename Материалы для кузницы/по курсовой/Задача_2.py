"""
Напишите функцию, которая получала бы список элементов чисел и возвращала бы долю единиц в списке

def count_for_ones(elements):
    pass

print(count_for_ones([1, 1, 0, 0]))  # вернет 0.5
print(count_for_ones([0, 0, 0, 0]))  # вернет 0.0
print(count_for_ones([1, 1, 1, 1]))  # вернет 1.0
"""

def count_for_ones(elements):
    return sum(elements) / len(elements)

result = count_for_ones([1, 1, 1, 1])
print(result)
