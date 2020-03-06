distance = int(input('Как много км пробежал спортсмен в 1й день? '))

goal = int(input('А сколько он должен пробежать? '))

day = 1

while distance < goal:
    distance = distance / 100 * 110
    day = day + 1

print(f'Спортсмен пробежит не менее {goal} км на {day}-й день')
