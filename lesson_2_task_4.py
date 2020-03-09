a = input('Введите несколько слов через пробел: ')

a = a.split(' ')
for idx, itm in enumerate(a):
    if len(itm) > 10:
        itm = itm[:10]
    print(idx, ': ', itm)

