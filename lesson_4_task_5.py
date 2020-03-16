from functools import reduce


def multiply(prev_el, el):
    return prev_el * el


print(reduce(multiply, [itm for itm in range(100, 1001) if not itm % 2]))