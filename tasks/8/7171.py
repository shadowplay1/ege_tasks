from itertools import product

items = list('БЖОУФЦЮ')
c = 0

for num, item in enumerate(product(items, repeat=4)):
    if num % 2 == 0 and item[0] == 'Ж' and item[1] == 'О':
        c += 1
        print(item, c)

print(c)
