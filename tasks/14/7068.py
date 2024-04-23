# 8GxI221 + 6EIxFC321 + 455Ex21 + D5Hx9559621 + KE7x21 + 8CGx33E621
# в системе 21
# % 20

digits = '0123456789abcdefghijk'
nums = []

for x in digits:
    s1 = int(f'8G{x}I221', 21)
    s2 = int(f'6EI{x}FC321', 21)
    s3 = int(f'455E{x}21', 21)
    s4 = int(f'D5H{x}9559621', 21)
    s5 = int(f'KE7{x}21', 21)
    s6 = int(f'8CG{x}33E621', 21)

    sum_ = s1 + s2 + s3 + s4 + s5 + s6

    if sum_ % 20:
        nums.append(sum_ // 20)

print(min(nums))