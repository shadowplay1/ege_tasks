from fnmatch import fnmatch
# пример решения с использованием fnmatch

# маска: 7*53?3*1
# найти числа в пределах 10^9, которые делятся на 2627
for i in range(0, 10 ** 9, 2627):
    if fnmatch(str(i), '7*53?3*1'):
        print(i, i // 2627)
