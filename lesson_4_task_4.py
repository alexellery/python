import random
numbers = [random.randint(1, 100) for itm in range(random.randint(1, 100))]
print(numbers)
for itm in numbers:
    if numbers.count(itm) == 1:
        print(itm)

