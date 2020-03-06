time = input('Введите любое количество секунд.')

sec = int(time) % 60
min = int(time) // 60 % 60
hour = int(time) // 3600

print(F' В часах это {hour} : {min} : {sec}')