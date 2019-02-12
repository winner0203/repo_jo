def calculate_change(payment, cost):
    change = payment - cost
    print("50000₩: %d" % (int(change / 50000)))
    change = change % 50000
    print("10000₩: %d" % (int(change / 10000)))
    change = change % 10000
    print("1000₩: %d" % (int(change / 1000)))

calculate_change(100000, 33000)


