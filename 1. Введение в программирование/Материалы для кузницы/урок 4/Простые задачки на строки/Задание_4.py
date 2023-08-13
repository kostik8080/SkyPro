lines = "A13f et3 D 5kk54 M"

numbers = 0

for line in lines:
    if line.isupper():
        numbers += 1

print(f"Заглавных букв {numbers}")
