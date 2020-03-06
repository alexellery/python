user_number = input('Введите целое положительное число любой величины.')
max = 0
n = 1
while int(user_number) > 0:
    n = int(user_number) % 10

    if n > max:
        max = n

    user_number = int(user_number) // 10

print(f"Наибольшая цифра: {max}")