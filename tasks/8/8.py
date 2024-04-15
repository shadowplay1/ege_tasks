from itertools import product,combinations,permutations
# func: product,combinations,permutations - методы для работы с комбинаторикой
# product,combinations - все возмомжные перестановки WORD
# permutations - все уникальные перетановки

# counter
c = 0

# func - one of (product,combinations,permutations)
for i in func('WORD', r=5):
    i = ''.join(i)
    
    if True: # condition
        c += 1

    print(c,i)

# made by isp
