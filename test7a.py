from collections import Counter

words = input().lower().split()
wordCount = Counter(words)

words = [word for word in wordCount]

# for key, value in wordCount.items():
#     print(key, value)

for element in wordCount:
    print(f'key: {element} count: {wordCount[element]}')

print(wordCount.most_common())