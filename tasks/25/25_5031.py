# 1?DED?CED

divider = int('79', 16)

start = int('10DED0CED', 16) // divider + 1
end = int('10DEF0CED', 16)

for i in range(start * divider, end + end, divider):
    s = hex(i)[2:]

    if s[0] == '1' and s[2:5] == 'ded' and s[6:9] == 'ced':
        print(i, i // 121)
