week = 52
money = 10
money_total = 0

for i in range(week):
    money_total += money
    print(f'第{i}周，存入{money}元，总计{money_total}元')
    money += 10

print(money_total)
