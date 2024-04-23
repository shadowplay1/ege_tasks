# 123x5 + 1x233
# в системе 68
# % 12

# 123x5 + 1x233
# ^^^^^   ^^^^^
# 43210   43210 (номера разрядов чисел)

nums = []
system = 68

for x in range(system):
    # ручной перевод в 10 систему счисления
    s1 = (1 * system ** 4) + (2 * system ** 3) + (3 * system ** 2) + (x * system ** 1) + (5 * system ** 0)
    s2 = (1 * system ** 4) + (x * system ** 3) + (2 * system ** 2) + (3 * system ** 1) + (3 * system ** 0)

    sum_ = s1 + s2

    if sum_ % 12 == 0:
        nums.append(sum_ // 12)

print(max(nums))
