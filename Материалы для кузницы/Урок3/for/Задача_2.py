"""# Телеграмма

# Превратите список в сообщение, замените "тчк" на "." "зпт" на ","

list_w_spaces = ["узнать", "зпт", "сделать", "зпт", "порадоваться", "тчк"]

# Пример ответа:
# узнать, сделать, порадоваться."""

list_w_spaces = ["узнать", "зпт", "сделать", "зпт", "порадоваться", "тчк"]

new_word = ""
for word in list_w_spaces:
    #print(word)
    res = "".join(list_w_spaces)
    rest = res.replace("зпт", ", ")
    rest = rest.replace("тчк", ". ")
print(rest)