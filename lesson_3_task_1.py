def division(a, b):
    if b:
        result = a / b
        return result
    else:
        return 'error, делить на 0 нельзя'


a = input('Введите число: ')
b = input('На что вы хотите его поделить? ')

print(division(int(a), int(b)))


