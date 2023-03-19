with open("myfile.txt", "w") as new:
    new.write("Hello file world!\n")

with open("myfile.txt", "r") as new:
    output = new.read()
    print(output)
