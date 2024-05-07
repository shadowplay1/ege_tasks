from fnmatch import fnmatch
c=0
for i in range(0,10**10,1917):
    if fnmatch(str(i),'3?12?14*5') and i%1917==0:
        print(i,i//1917)