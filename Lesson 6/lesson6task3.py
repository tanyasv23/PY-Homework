num = []
i = 1

while i <= 100:
    num.append(i)
    i += 1

print(num)

n = 0
m = []

while n < 100:
    if num[n]%5 and not num[n]%7:
        m.append(num[n])
    n += 1

print("\nResult: ", m)

