x = 1

while x <= 9:
    y = 1
    print("%d단 출력" %(x))
    while y <= 9:
        print("%d * %d = %d" % (x, y , x * y))
        y += 1
    print("")
    x += 1
    