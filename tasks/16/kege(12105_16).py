# 12105 
def f(n):
    return g(n-1)
def g(n):
    if n<10:
        return n
    return g(n-2)+1
def is_square(n):
    return n >= 0 and (int(n**0.5))**2 == n
k=0
for n in range(1, 100+1):
    if int((f(n))**0.5)**2 == f(n) and (f(n)>0):
        k += 1
print(k)
    