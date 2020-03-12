#возведение с помощью **

def raise_to_the_power(a, b):
    result = a ** b
    return result

#возведение с помощью *

def raise_to_the_power_2(a, b):
    i = 1
    y = 1
    while i <= (b * -1):
        y = y * a
        i += 1
    a = 1 / y
    return a


a = float(input('Введите действительное положительное число: '))
b = int(input('Введите целое отрицательное число: '))

print(raise_to_the_power(a, b))
print(raise_to_the_power_2(a, b))