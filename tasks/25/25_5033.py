r = [f'1{a}345{b}700' for a in '01234567' for b in '01234567']

d = int('114', 8)

for i in r:
    n = int(i, 8)

    if n % d == 0:
        print(n, n // d)
