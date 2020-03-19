def wages():
    hours = input('Введите количество отработанных часов: ')
    hourly_rate = input('Размер почасовой оплаты: ')
    bonus = input('Укажите размер премии: ')
    money = float(hours) * float(hourly_rate)
    return money + float(bonus)
print(f'Размер заработной платы составил: {wages()}')
