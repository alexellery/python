def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif b >= a and c >= a:
        return b + c
    else:
        return a + c

print(my_func(6, 10, 8))

