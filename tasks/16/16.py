digit = '0123456789abcdefghi'
for x in digit:
    s1 = int(f'98897{x}21',19)
    s2 = int(f'2{x}923',19)
    if (s1+s2)%18==0:
        print((s1+s2)//18,x)