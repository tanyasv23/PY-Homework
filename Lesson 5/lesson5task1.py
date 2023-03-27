import random

b = False
i = 0

while b == False:
    robot = random.randint(1, 10)
    user = input("Enter the number from 1 to 10: ")
    if 1 < int(user) > 10:
        b = False
        print("Enter correct number")
    elif int(user) == robot:
        b = True
        print ("You are right!")
    elif int(user) != robot:
        b = False
        print ("Right answer was", robot)
i +=1