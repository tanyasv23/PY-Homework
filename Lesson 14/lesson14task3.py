def arg_rules(max_length: int, type_: type, contains: list):
    def decorator(func):
        def wrapper(*param):
            for argument in param:
                if not isinstance(argument, type_):
                    print(f"Type error: current - {type(argument)}, valid - {type_}")
                    return False
                if len(argument) > max_length:
                    print(f"Lenght error: current - {len(argument)}, max - {max_length}")
                    return False
                if not all(symbol in argument for symbol in contains):
                    print(f"Content error: current - {argument}, should include - {contains}")
                    return False
            return func(*param)
        return wrapper
    return decorator

@arg_rules(max_length=15, type_=str, contains=['@', 'gmail.com'])
def gmail_f(gmail: str):
    print(f"{gmail} is validated")
    return True

result = gmail_f("user1@gmail.com")
print(result)
