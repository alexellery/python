my_list = []

a = input('Сколько чисел вы хотите ввести?')
i = 0
while i < int(a):
    my_list.append(int(input('Введите число')))
    i += 1

i = 0
while i < (len(my_list) - 1):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 2

print(my_list)