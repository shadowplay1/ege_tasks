'''
Дано число N (N <= 10^13), затем вводится N чисел. Найти количество пар чисел, произведение которых кратно 6.
Пара - любые 2 числа.
'''

n = int(input())
# k = [0] * 6

result = 0
nums = []

for i in range(n):
    num = int(input())
    nums.append(num)

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] * nums[j] % 6 == 0:
            result += 1

    # ost = num % 6
    # pair = (6 - ost) % 6

    # print('pair =', pair)
    # result += k[pair]
    # k[ost] += 1

print(result)
