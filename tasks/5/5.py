maxi=0
for n in range(4,10000):
    bi=bin(n)[2:]
    if n%5==0:
        add=bi[-3]+bi[-2]+bi[-1]
    else:
        add=bin((n%5)*5)[2:]
    ans=int(bi+add,2)
    if ans <=99:
        maxi=max(maxi,ans)
print(maxi)