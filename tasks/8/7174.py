from itertools import product

items = list('ГЛУБИНА')
c = 0

for i in product(items, repeat=7):
    str = ''

    for j in i:
        str += j

    try:
        ind = str.index('Г')

        if str[ind - 2] == 'А' and str[ind - 1] == 'И':
            c += 1
    except:
        pass

print(c)
