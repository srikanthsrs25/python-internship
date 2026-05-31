from collections import Counter

text = input("Enter text: ")

words = text.lower().split()

freq = Counter(words)

top_5 = freq.most_common(5)

print("\nTop 5 Words:")
for word, count in top_5:
    print(word, ":", count)