str1 = input("Ener the word: ")

strLenght = len(str1)
if strLenght < 2:
    print()
else:
    print(str1[0] + str1[1] + str1[-2] + str1[-1])
