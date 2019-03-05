def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

sample_temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(sample_temperature_list))
i = 0
while i < len(sample_temperature_list):
#    fahrenheit_to_celsius(sample_temperature_list[i])
    sample_temperature_list[i] = fahrenheit_to_celsius(sample_temperature_list[i])
    i = i +1
print("섭씨 온도 리스트: " + str(sample_temperature_list))
    
def krw_to_usd(won):
    return won / 1000 

def usd_to_jpy(dollars):
    return dollars * 125

amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))

i = 0
while i < len(amounts):
    amounts[i] = krw_to_usd(amounts[i])
    i = i + 1
print("미국화폐: " + str(amounts))

print(i)

i = 0
while i < len(amounts):
    amounts[i] = usd_to_jpy(amounts[i])
    i = i + 1
print("일본화폐: " + str(amounts))
    