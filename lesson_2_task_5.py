my_list = [1, 4, 2, 2, 6, 8, 7]

a = int(input('Оцените от 1 до 10 любое произведение искусства на ваш выбор: '))

if a in my_list:
    i = my_list.index(a)
    my_list.insert(i+1, a)
else:
    my_list.append(a)

print(my_list)
