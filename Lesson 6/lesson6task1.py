from random import randint

a = []
i = 0
k = 0

while i < 10:
    a.append(randint(1, 1000))
    k = max(a)
    i += 1

print (a)
print ("The largest number is: ", k)

