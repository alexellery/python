from os import path

file = open('task_3.txt', 'r+', encoding='UTF-8')
estrada = {}
for line in file:
    list = line.split()
    estrada[list[0]] = list[1]

for key, value in estrada.items():
    if int(value) < 20000:
        print(f'{key} получает меньше 20000')
avg = 0

for key, value in estrada.items():
    avg += int(value)

avg = avg // len(estrada)

print(f'Средняя зарплата {avg}')

file.close()