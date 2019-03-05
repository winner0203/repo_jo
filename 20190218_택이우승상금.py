INTEREST_RATE = 0.12
APARTMENT_PRICE = 1200000000

year = 1988
amount = 50000000

while year < 2016:
    amount = amount * 1.12
    year = year + 1   

if amount > APARTMENT_PRICE:
    print("%d원 차이로 아저씨의 말씀이 맞습니다" % (amount - APARTMENT_PRICE))
else: 
    print("%d원 차이로 아줌마의 말씀이 맞습니다" % (APARTMENT_PRICE - amount))





    