str1 = input("Enter the string: ")

strLenght = len(str1)
if strLenght < 2:
    print()
else:
    #v1
    print(str1[0] + str1[1] + str1[-2] + str1[-1])
    #v2
    print(str1[0:2] + str1[-2:])
