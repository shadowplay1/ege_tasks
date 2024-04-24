# 13082_15
def f(x,y):
    return (3*x+y>48) or (x>y) or (4*x+y<A)
for A in range(1000):
    if (all(f(x,y)for x in range(1000)for y in range(1000)))==0:
        print(A)

        # в данном задание max значение будет достигатся последним А



# made by isp
