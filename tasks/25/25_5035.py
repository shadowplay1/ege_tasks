r = [f'2{a}1{b}2{c}1{d}2{e}1' for a in '012' for b in '012' for c in '012' for d in '012' for e in '012']

def from_base_3(x):
    r = 0
    d = 0

    while x > 0:
        d = d + x % 10 * 3 ** r
        r += 1
        x //= 10

    return d

d = from_base_3(114)

for i in r:
    n = from_base_3(int(i))

    if n % d == 0:
        print(n, n // d)
