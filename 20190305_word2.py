data = open('vocabulary.txt', 'r')

eng = []
kor = []
kor_word = 0

for line in data:
    data = line.strip().split(": ")
    eng.append(data[0])
    kor.append(data[1])

i = 0
while i < len(eng):
    kor_word = raw_input("%s: " %(eng[i]))
    if kor_word == kor[i]:
        print("정답입니다.")
    else:
        print("정답은 %s입니다." %(kor[i]))
    i = i + 1

data.close()