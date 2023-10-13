money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count = 0
1
while True:
    if money_capital + salary >= spend:
        count += 1
        money_capital -= (spend - salary)
        spend += spend * increase
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", count)
