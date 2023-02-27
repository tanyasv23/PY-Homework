from random import randint

list1 = []
list2 = []

n = 0

while n < 10:
    list1.append(randint(1, 10))
    list2.append(randint(1, 10))
    n += 1

print(list1)
print(list2)

list3 = []
i = 0

while i < 10:
    j = 0
    while j < 10:
        if list1[i] == list2[j] and list1[i] not in list3:
            list3.append(list1[i])
        j += 1
    i += 1

print("Common: ", list3)