file = open('task_1.txt', 'r+', encoding='UTF-8')
line = input('Введите что-нибудь: ')

while line:
    file.writelines(line + '\n')
    line = input('Введите что-нибудь: ')

file.close()
file = open('task_1.txt', 'r+', encoding='UTF-8')

print(file.read())

file.close()
