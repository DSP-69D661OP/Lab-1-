money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 0
money_capital = money_capital - spend + salary
while(money_capital >= 0):
    a = spend * increase
    spend = spend + a

    deduction = spend - salary

    money_capital = money_capital - deduction

    month = month + 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
