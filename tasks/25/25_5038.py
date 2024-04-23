r = [f'12345{a}6{b}8' for a in '0123456789' for b in '0123456789']

for i in r:
    if int(i) % 17 == 0:
        print(i, int(i) // 17)
