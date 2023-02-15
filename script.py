# счетчики
count1 = 0
count2 = 0
count3 = 0

#цена билета в категориях возраста
sum1 = 0
sum2 = 990
sum3 = 1390

ticket = int(input("Сколько билетов Вы желаете приобрести? "))

for a in range(1, ticket + 1):
    age = int(input(f"Введите возраст посетителя для билета #{a}: "))
    if age < 18:
        count1 += 1
        print(f"Цена за билет: {sum1}")
    elif 18 <= age <= 25:
        count2 += 1
        print(f"Цена за билет: {sum2}")
    elif age > 25:
         count3 += 1
         print(f"Цена за билет: {sum3}")

all_summa = count1*sum1 + count2*sum2 + count3*sum3

if ticket > 3:
    print("Общая сумма: ", all_summa)
    print("Сумма с учетом скидки", all_summa - all_summa / 10)
else:
    print("Общая сумма: ", all_summa)
