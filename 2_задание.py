salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 1000
months = 9
while(months > 0):
    a = spend * increase
    #a = int(a)
    spend = a + spend
    money_capital = money_capital + spend - salary

    months = months - 1

print(f"Подушка безопасности, чтобы протянуть 10 месяцев без долгов:",int(money_capital))

