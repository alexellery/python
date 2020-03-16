from itertools import count

for itm in count(15):
        print(itm)


from itertools import cycle

for el in cycle(['я', 'люблю', 'мандарины']):
    print(el)