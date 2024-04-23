# 615x483 + 85996x262 + 62421x + 45x61584x
# в системе 13
# % 12

digits = '0123456789abc'
nums = []

for x in digits:
    s1 = int(f'615{x}483', 13)
    s2 = int(f'85996{x}262', 13)
    s3 = int(f'62421{x}', 13)
    s4 = int(f'45{x}61584{x}', 13)

    sum_ = s1 + s2 + s3 + s4

    if sum_ % 12 == 0:
        nums.append(sum_ // 12)
    
print(max(nums))
