from random import randint

a = []
i = 0
k = 0

while i < 10:
    a.append(randint(1, 1000))
    if a[i] > k:
        k = a[i]
    i += 1

print (a)
print ("The largest number is: ", k)

