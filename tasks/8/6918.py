from itertools import product

items = ['А', 'И', 'М', 'Р' 'Я']
for index, item in enumerate(product(items, repeat=5)):
    if index + 1 == 211:
        print(item)
