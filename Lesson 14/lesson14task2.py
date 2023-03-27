def stop_words(words: list):
    def decorator(func):
        def wrapper(*param):
            result = func(*param)
            if isinstance(result, str):
                for word in words:
                    result = result.replace(word, "*")
            return result
        return wrapper
    return decorator

@stop_words(['jam', 'toast', 'breakfest'])
def create_slogan(name: str) -> str:
    return f"{name} eats toast with jam for breakfest"

result = create_slogan("Mark")
print(result)
