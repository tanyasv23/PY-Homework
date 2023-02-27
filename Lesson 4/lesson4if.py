import math

#task1

print("Task 1")

x = False
l = 0

while x == False:
    age = input ("Enter your age: ")
    if age.isdigit() == True:
        if int(age) >= 18:
            print("You are the adult")
            x = True
        else:
            print("You are the child")
            x = True
    else:
        print("Please enter correct age")
    l += 1


#task2

print("\nTask 2")

u = False
n = 0

while u == False:
    y = input("Enter the number: ")
    if y.isdigit():
        m = int(y)%5
        if m == 0:
            print("Ділиться на 5")
            u = True
        else:
            print("Не ділиться на 5")
            u = True
    else:
        print("Enter correct number")

    n += 1


#task3

print("\nTask 3")

d = False
e = 0

while d == False:
    a = input("Enter 1 number: ")
    b = input("Enter 2 number: ") 
    if a.isdigit() and b.isdigit():
        if int(a) < int(b):
            print("Max: " + b, "\n" + "Min: " + a)
            d = True
        elif int(a) > int(b):
            print("Max: " + a, "\n" + "Min: " + b)
            d = True
        else:
            print (a, "is equal to", b)
            d = True
    else:
        print("Wrong data. Try again")
e += 1

#task4

print("\nTask 4")

s = False
w = 0


while s == False:
    point = input("Введіть оцінку від 1 до 5: ")
    if point.isdigit() == True:
        if int(point) == 1:
            print("погано")
            s = True
        elif int(point) == 2:
            print("незадовільно")
            s = True
        elif int(point) == 3:
            print("задовільно")
            s = True
        elif int(point) == 4:
            print("добре")
            s = True
        elif int(point) == 5:
            print("відмінно")
            s = True
        else:
            print("Помилка, введіть число від 1 до 5")
    else:
        print("Помилка, введіть число від 1 до 5")
w += 1

#task5

print("\nTask 5")

count = 1
c = 0
negative = 0
positive = 0
numbers = "01234566789-"



while c < 3:
    g = input(f"Enter number {count}: ")

    def func(g, numbers):
        for char in g:
            if not char in numbers:
                return False
        return True

    if func(g, numbers) == False:
        print ("Number is incorrect. Please try again")
        c -= 1
        count -= 1
    elif int(g) >= 0:
        positive += 1
    else:
        negative +=1
    c +=1
    count += 1

print ("Positive: ", positive)
print ("Negative: ", negative)


#task6 

print("\nTask 6")

r = False
q = 0

while r == False:
    j = input("Введіть число від 10 до 100: ")

    if j.isdigit() == True:
        if int(j) > 100 or int(j) < 10:
            print("Error")

        elif int(j) <= 20:
            print("Low")
            ask = input ("Enter 1 if you want to enter one more number: ")
            if ask == "1":
                r == False
            else:
                r = True
                print("Programm is closed") 

        elif 50 > int(j) > 20:
            print("Middle")
            ask = input ("Enter 1 if you want to enter one more number: ")
            if ask == "1":
                r == False
            else:
                r = True 
                print("Programm is closed")       
            
        elif int(j) >= 50:
            print ("Big")
            ask = input ("Enter 1 if you want to enter one more number: ")
            if ask == "1":
                r == False
            else:
                r = True
                print("Programm is closed")     

    else:
        print("Error")

    q +=1
    