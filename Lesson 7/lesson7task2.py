stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total = 0
sum = 0

for i in stock:
    if stock[i] > 0:
        sum = stock[i] * prices[i]
        total += sum

print("Total price is:", total)