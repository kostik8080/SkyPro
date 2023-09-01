"""
В функцию передается закодированное в прошлом задании строкой число. Превратите его обратно в число,
 используя словарь letters_to_nums. Обратите внимание, результат должен быть в виде int!
letters_to_nums = {
  "A": "1" ,
  "B": "2" ,
  "C": "3" ,
  "D": "4" ,
  "E": "5" ,
  "F": "6" ,
  "G": "7" ,
  "H": "8" ,
  "I": "9" ,
  "J": "0" ,
}

def decode(encoded_number):
   pass


print(decode("CDE")) # вернет 345
print(decode("IJJJ")) # вернет 9000

"""

letters_to_nums = {
  "A": "1" ,
  "B": "2" ,
  "C": "3" ,
  "D": "4" ,
  "E": "5" ,
  "F": "6" ,
  "G": "7" ,
  "H": "8" ,
  "I": "9" ,
  "J": "0" ,
}

# def decode(encoded_number):
#    string_int = encoded_number
#    number = 0
#    for num in string_int:
#        number = letters_to_nums.keys()
#    return number

def decode(encoded_num):
    encoded_str = encoded_num
    decoded_num = 0

    for letter in encoded_str:
        char_int = letters_to_nums[letter.upper()]
        if char_int:
            decoded_num *= 10
            decoded_num += int(char_int)

    return decoded_num
# encoded_string = "CDE"
# decoded_number = decode_number(encoded_string)
# print(decoded_number) # 345


# def code_nums_to_letters(number):
#     number_string = str(number)
#     letters_str = ""
#     for string in number_string:
#         letters_str += nums_to_letter[string]
#     return letters_str


print(decode("CDE")) # вернет 345
print(decode("IJJJ")) # вернет 9000