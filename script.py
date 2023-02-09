money = int(input("Введите сумму средств: "))
per_cent = {'ТКБ': 5.6,
            'СКБ': 5.9,
            'ВТБ': 4.28,
            'СБЕР': 4.0
            }
deposit = list(map(round, [per_cent['ТКБ']*money/100, per_cent['СКБ']*money/100, per_cent['ВТБ']*money/100, per_cent['СБЕР']*money/100]))
print(deposit)
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать —", max_deposit)

#print("В ТКБ вы накопите %d за год вклада" % (per_cent['ТКБ']*float(money)))
#print("В СКБ вы накопите %d за год вклада" % (per_cent['СКБ']*float(money)))
#print("В ВТБ вы накопите %d за год вклада" % (per_cent['ВТБ']*float(money)))
#print("В СБЕР вы накопите %d за год вклада" % (per_cent['СБЕР']*float(money)))