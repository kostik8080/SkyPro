words = ["abcd", "ab", "bcdef"]

word_dict = {}

for i, word in enumerate(words):
    word_dict[i] = len(word)
print(word_dict)