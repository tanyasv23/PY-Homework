name = "tanya"
inp = input("Please enter your name ")
nameLen = len(name)
inpLen = len(inp)
i = 0

if nameLen != inpLen:
    print (False)
else:
    if name.lower() == inp.lower():
        print (True)
    else:
        print (False)

 
     
