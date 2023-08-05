letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]

letters_1 = []
letters_2 = []

for letter in range(len(letters)):
    if letter % 2 == 0:
        letters_1.append(letters[letter])


    else:
        letters_2.append(letters[letter])

print(letters_1)
print(letters_2)
