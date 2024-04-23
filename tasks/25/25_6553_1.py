# 1000000000
# 20?????23

gen = [f'20{a}{b}{c}{d}{e}23' for a in '012356789' for b in '012356789' for c in '012356789' for d in '012356789' for e in '012356789']

for i in gen:
    num = int(i)
    sum_of_numbers = sum(list(map(int, list(i)))) 
    
    if num % 2023 == 0 and sum_of_numbers % 7 == 0 and sum_of_numbers < 20:
        print(num, num // 2023)

# 1?DED?CED

divider = 2023

start = 20023 // divider + 1
end = 10 ** 9

for i in range(start * divider, end, divider):
    s = hex(i)[2:]

    if s[0:2] == '20' and s[-2:] == '23':
        print(i, i // 121)

