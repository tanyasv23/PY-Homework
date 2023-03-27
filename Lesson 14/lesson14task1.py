def f(func):
    def wrapper(*params):
        print(f"Name - {func.__name__}\nParams - {params}")
        return func(*params)
    return wrapper

@f
def result(a, b):
    a = pow(a, b)
    return a

result(5, 3)
