from attr.validators import max_len

text = input("Text: ")

#拆分单词
words = text.split()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# max_length = max(len(word) for word in word_counts)#找出最长的单词用来对齐,可有可无

for word in sorted(word_counts):#sorted()首字母排序
    # print(f"{word:{max_length}} : {word_counts[word]}")
    print(f"{word} : {word_counts[word]}")

