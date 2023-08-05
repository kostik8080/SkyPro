line = "13f et3 5kk 54"

score_number = 0
score_string = 0

for char in line:
    if char.isalpha():
        score_string += 1
    elif char.isdigit():
        score_number += 1

print(score_string)
print(score_number)