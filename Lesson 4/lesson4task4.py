name = "tanya"
inp = input("Please enter your name ") # Tanya
nameLen = len(name)
inpLen = len(inp)

#v1
if nameLen != inpLen:
    print ("V1 Result: ", False)
else:
    if name.lower() == inp.lower():
        print ("V1 Result: ", True)
    else:
        print ("V1 Result: ", False)

#v2
i = 0
if nameLen == inpLen:
    while i < nameLen:
        if name[i].upper() != inp[i].upper():
            print("V2 Result: ", False)
            break
        elif i == nameLen - 1:
            print ("V2 Result: ", True)
        i += 1
else:
    print("V2 Result: ", False)
