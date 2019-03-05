data = open('voca.txt','r')

for line in data:
    data = line.strip().split(': ')
    answer = input('%s: ' % (data[1]))
    if answer == data[0]:
        print("OK !!!")
    else:
        print("정답은 %s야" % (data[0]))

data.close()

