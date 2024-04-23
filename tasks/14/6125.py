# 12x4598 (98) + 1x98123 (123)
# ^^^^^^^        ^^^^^^^
# 6543210        6543210

# % 123

system1 = 98
system2 = 123

nums = []

for x1 in range(system1):
    for x2 in range(system2):
        s1 = (1 * system1 ** 6) + (2 * system1 ** 5) + (x1 * system1 ** 4) + (4 * system1 ** 3) + (5 * system1 ** 2) + (9 * system1 ** 1) + (8 * system1 ** 0)
        s2 = (1 * system2 ** 6) + (x2 * system2 ** 5) + (9 * system2 ** 4) + (8 * system2 ** 3) + (1 * system2 ** 2) + (2 * system2 ** 1) + (3 * system2 ** 0)

        sum_ = s1 + s2

        if sum_ % 123 == 0:
            nums.append(sum_ // 123)

print(max(nums))
