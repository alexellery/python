income = int(input('Сколько ваша фирма заработала в этом месяце?'))

spendings = int(input('А какие издержки вы понесли?'))

if income > spendings:
    print(f'Вы вышли в плюс! Ваша прибыль составила {income - spendings}, что составляет {(income - spendings) / income * 100}% выручки')
    staff = input('Сколько человек работает в вашей фирме?')
    print(f'Ух ты, ваша фирма получила {(income - spendings) // int(staff)} монет на каждого сотрудника!')
elif income == spendings:
    print('Вы вышли в ноль!')
else:
    print(f'Ваша фирма в минусе. Вы понесли убытки в размере {spendings - income} монет')

