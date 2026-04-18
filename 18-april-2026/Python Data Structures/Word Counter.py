sentence = "python is easy and python is powerful"
words = sentence.split()
word_count = {word: words.count(word) for word in set(words)}

print(word_count)