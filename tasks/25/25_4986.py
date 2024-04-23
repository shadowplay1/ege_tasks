def is_palindrome(n: int) -> bool:
    s = str(n)
    rev = ''.join(list(reversed(s)))

    return s == rev


def get_dividers(n: int) -> bool:
    for i in range(2, n // 2 -1):
        if n % i == 0:
            return False

    return True

groups: list[dict[int, int]] = []


for i in range(100, 10 ** 9):
    nums = list(str(i))
    res = 0

    groups.append({36: 3})
    for n in nums:
        if not n == '0':
            res *= int(n)

# print(get_dividers(int(input())))
