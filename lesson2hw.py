# task2

print("Task2 result: \n")
a = 'sum'
b = 9+8

#sum = 17
print(a, b, sep = ' = ')


c = input("Enter your age: ")
print(c)
d = "Your age is: "

# Your age is: 21
print(d, end = c)
print("\n")



# task3 v1

v1 = "#"
v6 = "# # # # # #"
sp = '         '
print ("Here is the output of v1:\n")
print (v6, "\t")
print (v1, v1, sep = sp)
print (v1, v1, sep = sp)
print (v1, v1, sep = sp)             
print (v1, v1, sep = sp)
print (v1, v1, sep = sp)
print (v6, "\t")
print("\n")
print (v1, v1, sep = sp)
print (v1, v1, sep = sp)
print (v1, v1, sep = sp)
print (v6, "\t")
print (v1, v1, sep = sp)
print (v1, v1, sep = sp)
print (v1, v1, sep = sp)
print("\n")


# task3 v2

print ("Here is the output of v2:\n")

p = "#"
i = 0
x = 0
y = 0

while i < 5:
    print(p, end = ' ')
    i+=1

while x < 6:
    if x == 0:
        print(p)
    else:
        print(p, p, sep = "         ")
    x +=1

    if x == 6:
        while y < 6:
            print(p, end = " ")
            y +=1


print ("\n")

r = 0
k = 0
d = 0

while k < 7:
    if k != 3:
        print(p, p, sep = "         ")
    else:
        print(p)
    k +=1
    if k == 3:
        while r < 5:
            print(p, end = ' ')
            r+=1
            


