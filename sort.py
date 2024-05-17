# sentence = "can IT count this test when this test has many words"


# sentence = sentence.replace(',', '').lower().split()

# dict = {}



# # keys = exists
# for word in sentence:
#     if word in dict.keys():
#         dict[word] += 1
#     else:
#         dict[word] = 1
        
# print(dict)

sentence = "can IT count this test when this test has many words"
words = sentence.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

print("Most common words:")
for word, count in sorted_count:
    print(f"{word}: {count}")
