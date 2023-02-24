dic = {}
a = input("Please enter the string: ")
i = 0
word = a.split()
print(word)
l = len(word)

while i < l:
    if word[i] not in dic:
        dic[word[i]] = 1
    else:
        dic[word[i]] += 1
    i += 1
print (dic)


