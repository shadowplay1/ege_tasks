# 1000000000
# 20*23
# 2023

gen = [f'20{a}{b}{c}{d}{e}23' for a in '01234567' for b in '01234567' for c in '01234567' for d in '01234567' for e in '01234567']

for i in gen:
    num = int(i)
    sum_of_numbers = sum(list(map(int, list(i)))) 
    
    if num % 2023 == 0 and sum_of_numbers % 7 == 0 and sum_of_numbers < 20:
        print(num, num // 2023)
