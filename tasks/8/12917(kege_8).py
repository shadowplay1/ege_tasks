# 12917
from itertools import *
c=0
i=[''.join(x) for x in permutations('просто')]
print(len(set([z for z in i if not any(z[q] == z[q+1] for q in range(len(z)-1))])))


# made by isp
