f = open('9_2024.csv').readlines()
count = 0

for i in f:
    row: list[int] = list(map(int, i.split(';')))
    nums: dict[int, int] = {}

    for j in row:
        if j not in nums:
            nums[j] = 1
        else:
            nums[j] += 1


    local_sum = 0

    for j in nums:
        if nums[j] == 2:
            local_sum += j
    
    # среднее арифметичекое по строке в файле (длина строки - 7)
    sr_row = sum(row) / 7

    if (local_sum / 2) < sr_row:
        # считаем количество раз, когда число в строке повторяется дважды
        count_of_2 = ''.join(map(str, nums.values())).count('2')

        if len(set(row)) == 5 and count_of_2 == 2:
            count += 1

print(count)
