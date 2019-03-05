data = open('chicken.txt', 'r')

sum = 0
day = 0

for line in data:
    data = line.strip().split(": ")
    print(data)
    sum = sum + int(data[1])
    day = day + 1
    print(data)

print(sum / day)