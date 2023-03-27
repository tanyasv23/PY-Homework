def f1(var1):
    def f2(var2):
        return var1 * var2
    return f2

function = f1(2)
result = function(8)

print(result)