str1 = "hello world python programming"

words = str1.split()

result = []

for i in range(len(words)):
    if i % 2 == 0:
        result.append(words[i].upper())
    else:
        result.append(words[i])

print(" ".join(result))
