"""
# Вывести все элементы списка кроме слов "Пропуск" при помощи  while

keywords = ["Желание", "Семнадцать", "Пропуск", "Ржавый", "Пропуск", "Печь" ]

# Пример ответа:

# Желание Семнадцать Ржавый Печь
"""

keywords = ["Желание", "Семнадцать", "Пропуск", "Ржавый", "Пропуск", "Печь" ]

i = -1
while (i < len(keywords)-1):
    keyword = keywords[i+1].strip()
    if keyword == "Пропуск":
        pass
    elif keyword != "Пропуск":
        print(keyword)
    i += 1
print() # для разделения списка оставшихся элементов
