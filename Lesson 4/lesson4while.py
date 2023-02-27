#1
print("Task 1")

f = 0
while f < 10:
    print(20)
    f += 1

print ("\n")


#2
print("Task 2")

t = 1
while t <= 50:
    print (t)
    t +=1

print ("\n")


#3
print("Task 3")
i = 0
p = 0

while i < 10:
    k = input("Enter the number: ")

    if k.isdigit() == True:
        p += int(k)
    else:
        print("Wrong number. Try again")
        i -= 1
    i +=1

print("Sum is:", p)
