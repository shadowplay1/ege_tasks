start = 245_690
end = 245_756

nums: list[tuple[int, int]] = []

def get_dividers(n):
    dividers = 0

    for i in range(1, n // 2 + 1):
        if i % i == 0:
            dividers += 1

for index, i in list(enumerate(range(start, end + 1))):
    dividers = get_dividers(i)
    
    if dividers == 2:
        nums.append((i, index))

print(nums)
