ns = []

def convert(n: int, base: int) -> str:
    converted = ''
    
    while n > 0:
        remainder = n % base
        converted = str(remainder) + converted

        n = n // base

    return converted

for n in range(500):
    t = convert(n, 6)

    remainder = n % 3
    
    if remainder == 0:
        t += t[:2]
    else:
        multiplied_remainder = remainder * 10

        converted_remainder = convert(multiplied_remainder, 6)
        t += converted_remainder
    
    r = int(t, 6)

    if r > 680:
        ns.append(r)

print(min(ns))
