def print_grade(mid, fin):
    total = mid + fin
    if total >= 90:
        print('a')
    elif total >= 80:
        print('b')
    elif total >= 70:
        print('c')
    else :
        print('f')

print_grade(10,70)
