hesh_tags = "сегодня #прогулка# #еда #ко#ты"
words = hesh_tags.split(" ")

total = 0

for word in words:
    if word.startswith("#"):
        total += 1

print(total)