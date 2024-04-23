from itertools import permutations

num_groups = list(permutations(range(0, 7), 6))
all_nums: list[str] = []

for i in num_groups:
    num_string = ''
    for j in i:
        num_string += str(j)
    
    all_nums.append(num_string)

print(all_nums)





# 1000000000
# 20*23
# 2023

# l = ['']

# for a in '01234567':
#     for b in '01234567':
#         for c in '01234567':
#             for d in '01234567':
#                 for e in '01234567':
                    