daysList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

i = 0

week1 = {i+1: daysList[i] for i in range(7)}
week2 = {day: i for i, day in week1.items()}

print(week1)
print(week2)