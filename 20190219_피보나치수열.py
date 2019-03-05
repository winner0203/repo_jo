# 변수
previous = 0
current = 1
i = 0

while i < 20:
    print(current)
    temp = previous
    previous = current
    current = previous + temp
    i = i + 1