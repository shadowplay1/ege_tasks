def del_(n,m):
    return n%m==0
def f(x,A):
    return (not(del_(x,A))) <= (del_(x,14) <= (not(del_(x,4))))
for A in range(1,1000):
    if (all(f(x,A) for x in range(1000)))==1:
        print(A)