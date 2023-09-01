"""
nums_to_letter = {
"1": "A",
"2": "B",
"3": "C",
"4": "D",
"5": "E",
"6": "F",
"7": "G",
"8": "H",
"9": "I",
"0": "J",
}

def code_nums_to_letters(number):
    ...

print(code_nums_to_letters(15)) #>>> "AE"
print(code_nums_to_letters(101)) #>>> "AJA"
"""
nums_to_letter = {
"1": "A",
"2": "B",
"3": "C",
"4": "D",
"5": "E",
"6": "F",
"7": "G",
"8": "H",
"9": "I",
"0": "J",
}


def code_nums_to_letters(number):
    number_string = str(number)
    letters_str = ""
    for string in number_string:
        letters_str += nums_to_letter[string]
    return letters_str


print(code_nums_to_letters(15))  # >>> "AE"

print(code_nums_to_letters(101))  # >>> "AJA"
