def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1
def fn(x):
    A = '0' + x + '0'
    while '00' not in A:
        A = A.replace('02','101',1).replace('11','2',1).replace('012','30',1).replace('010','00',1)
    return 1 if prime(sum(map(int, list(A)))) else 0
print(min([i for i in range(41,200) if fn('1' * 40 + '2' * i)]))