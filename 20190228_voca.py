out_file = open('new_file.txt', 'w')

i = 1

while i <= 2:
    eng_mean = input('영어: ')
    if eng_mean == 'q':
        break 
    kor_mean = input('한국어: ')
    if kor_mean == 'q':
        break
    else:
        out_file.write("%s: \n%s" % (eng_mean, kor_mean))

out_file.close()