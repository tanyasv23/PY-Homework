name = input ("Enter your name: ")
numbers = "0123456789"
checkName = name.isalpha()

i = 0
while not checkName:
    name = input ("Incorrect name! Enter your name again: ")
    checkName = name.isalpha()
    i += 1

age = input ("Enter your age: ")
   
p = 0
res = False

while res == False:
    if age.isdecimal():
        final = int(age) + 1
        if 0 <= final <= 100:
            print(f"Hello {name}, on your next birthday you’ll be {final} years")
            res = True
        else:
            age = input ("Incorrect age! Enter your age again: ")
            res = False   
    else:
        age = input ("Incorrect age! Enter your age again: ")
        res = False
        
    p += 1


