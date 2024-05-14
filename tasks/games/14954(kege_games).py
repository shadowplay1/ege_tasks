# 14954 
def f(k1,k2,k3,m):
    if any(x for x in [k1,k2,k3])==20 or (k1+k2+k3)>=25:return m%2==0
    if m==0:return 0
    #  удваивает число камней в какой-то куче или добавляет по два камня в каждую из куч
    h = [f(k1*2,k2,k3,m-1),f(k1,k2*2,k3,m-1),f(k1,k2,k3*2,m-1),f(k1+2,k2+2,k3+2,m-1)]
#     return any(h) if (m-1)%2==0 else all(h) 19 
# print([s for s in range(1,19) if f(2,3,s,2)])
#     return any(h) if (m-1)%2==0 else all(h) 20
# print([s for s in range(1,19) if not f(2,3,s,2) and f(2,3,s,3)])
    return any(h) if (m-1)%2==0 else all(h) 21
print([s for s in range(1,19) if not f(2,3,s,2) and f(2,3,s,4)])