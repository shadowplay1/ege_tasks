# 6782
from itertools import *
c=0
for i in product('01234567',repeat=6):
    i=''.join(i)
    # print(i)
    if i[0]!='0':
        i=i.replace('7','*').replace('5','*').replace('3','*').replace('1','*')
        # print(i)
        if i.count('6') ==2 and ('*6*' not in i and  '*6' not in i and  '6*' not in i):
            c+=1
            
print(c)

# made by isp