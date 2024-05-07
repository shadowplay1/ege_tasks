f = open('txt/9.txt').readlines()
arr = [list(map(int, x.split())) for x in f]
max_row_number = 0

def repeat_(arr):
    dict_ = {}
    for num in arr:
        if num in dict_:
            dict_[num] += 1
        else:
            dict_[num] = 1
    for n, k in dict_.items():
        if k == 3:
            return n
    return None

for i in range(len(arr)):
    povtor = repeat_(arr[i])
    if povtor is not None:
        mas = [x for x in arr[i] if x != povtor]
        if len(mas) == 4 and ((povtor * 3 + sum(mas)) / 7) > (sum(mas) / 4):
            max_row_number = i + 1

print(max_row_number)
