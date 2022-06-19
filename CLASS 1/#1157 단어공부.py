word = input().lower()
word_set = list(set(word))
count = []

for i in word_set:
    num = word.count(i)
    count.append(num)

if count.count(max(count)) >= 2:
    print("?")
else:
    print(word_set[(count.index(max(count)))].upper())