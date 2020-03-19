file = open('task_4.txt', 'r', encoding='UTF-8')

translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []

for line in file:
    list = line.split(' ', 1)
    for key, value in translation.items():
        if list[0] == key:
            new_file.append(value + ' ' + list[1])

file.close()

with open('task_4_2.txt', 'w', encoding='UTF-8') as file_2:
    file_2.writelines(new_file)

with open('task_4_2.txt', 'r', encoding='UTF-8') as file_2:
    print(file_2.read())
