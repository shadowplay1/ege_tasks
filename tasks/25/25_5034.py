r = [f'1{a}1{b}1{c}1{d}1{e}{f}1' for a in '01' for b in '01' for c in '01' for d in '01' for e in '01' for f in '01']

divider = int('101101', 2)

for i in r:
    n = int(i, 2)

    if n % divider == 0:
        print(n, n // divider)
