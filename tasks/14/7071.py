# 819x6x32 + 45656925x + 771377x1

digits = '0123456789abcdefg'
nums = []

for x in digits:
    s1 = int(f'819{x}6{x}32', 17)
    s2 = int(f'45656925{x}', 17)
    s3 = int(f'771377{x}1', 17)

    sum_ = s1 + s2 + s3

    if sum_ % 16 == 0:
        nums.append(sum_ // 16)

print(max(nums))