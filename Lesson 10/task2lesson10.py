def inp():
    try:
        a = float(input("a "))
        b = float(input("b "))
        c = print(pow(a, 2)/b)
        return c
    except ValueError:
        print("Wrong values")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except:
        print("Error")

inp()
