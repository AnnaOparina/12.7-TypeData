bilets = int(input('Введите количество приобретаемых билетов: '))
age1 = 0
age2 = 0
age3 = 0
Age = age1+age2+age3
Prices = age2*990+age3*1390
for i in range(bilets):
    age = int(input('Введите возраст посетителя:  '))
    if age < 18:
        age1 += 1
    elif 25 <= age >= 18:
        age2 += 1
    else:
        age3 += 1
if Age <= 3:
    print("Сумма к оплате: ", Prices)
else:
    print('Вам предоставлена скидка 10% \n Сумма к оплате: ', int(Prices-Prices*10/100))
