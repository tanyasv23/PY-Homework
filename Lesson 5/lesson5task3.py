import random

word = input("Enter the word: ")
lt = list(word)

i = 0

while i < 5:
    a = random.shuffle(lt)
    print(''.join(lt))
    i += 1

