money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
i = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while True:
    money_capital += salary
    if money_capital >= spend:
        money_capital -= spend
        spend = spend + (spend * 0.05)
        i += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", i)
