from itertools import product

items = [5, 6, 7]
c = 0

for i in product(items, repeat=12):
    n = ''
    
    for num in i:
        n += str(num)
    
    if not n.count('55'):
        c += 1
    
print(c)

    
