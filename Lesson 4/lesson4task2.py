phoneNumber = input("Please enter your phone number: ")
numbers = "0123456789"
lenCheck = len(phoneNumber)
 

def phone(phoneNumber, numbers):
    for char in phoneNumber:
        if not char in numbers:
            return False
    return True
        

if phone(phoneNumber, numbers) == True:
    if lenCheck != 10:
        print("Error! Phone number should contain 10 numbers\n")
    else:
        print("Phone number is correct\n")
else:
    print ("Error! Phone number should contain only numbers\n")
