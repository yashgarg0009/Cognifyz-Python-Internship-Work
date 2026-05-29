# Task: File Manipulation
# Write a Python program that reads a text
# file and counts the occurrences of each
# word in the file. Display the results in
# alphabetical order along with their
# respective counts.

file = open("sample.txt", "r")

text = file.read().lower()
words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in sorted(word_count):
    print(word, ":", word_count[word])

file.close()