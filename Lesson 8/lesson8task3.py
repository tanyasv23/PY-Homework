def make_operation(operator, *numbers):
    if operator == '+':
        return sum(numbers)
    elif operator == '-':
        return numbers[0] - sum(numbers[1:])
    elif operator == '*':
        result = 1
        for i in numbers:
            result *= i
        return result
    else:
        print("Error")
    

print(make_operation('+', 84, 22, 12)) 
print(make_operation('-', 30, 76, 8))
print(make_operation('*', 9, 15, 3))
print(make_operation('/', 7, 2, 1))