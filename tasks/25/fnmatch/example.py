from fnmatch import fnmatch

for i in range(0, 10 ** 9, 2627):
    if fnmatch(str(i), '7*53?3*1'):
        print(i, i // 2627)
