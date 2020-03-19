file = open('task_2.txt', 'r+', encoding='UTF-8')
lines_letters = {}
lines = 0

for line in file:
    lines += 1
    letters = len(line)
    lines_letters[lines] = letters

for key, value in lines_letters.items():
    print(f'В {key} строке {value} букв')
print(f'Всего строк {lines}')

file.close()