# 8417
from itertools import *
c=0
for i in permutations('ярослав',r=5):
    
    i=''.join(i)
    
    i=i.replace('р','*').replace('с','*').replace('л','*').replace('в','*')
    i=i.replace('я','/').replace('о','/').replace('а','/')
    if (i.count('*') > i.count('/')) and '//' not in i:
        c+=1
print(c)


# made by isp
