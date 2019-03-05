rfile = open('chicken.txt', 'r')
sum = 0
day = 0
for line in rfile:
    data =line.split(": ")
    sum = sum + int(data[1])
    day = day + 1

print(sum/day)




