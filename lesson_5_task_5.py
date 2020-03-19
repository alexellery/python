from functools import reduce

def sum(prev_el, el):
    return prev_el + el


with open('task_5.txt', 'w', encoding='UTF-8') as file:
    file.write('1 2 3 4 5 6 4 56 4 67 5 2 34 5 346')

with open('task_5.txt', 'r+', encoding='UTF-8') as file:
    num = file.read().split()

print(reduce(sum, [int(itm) for itm in num]))

