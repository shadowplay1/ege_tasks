# 10104
def f(x,y):
    if x==y:
        return 1 
    # не включает 11 
    if x>y or x==11:
        return 0 
    return f(x+1,y)+f(x*2,y)+f(x**2,y)
print(f(2,20))

# made by isp