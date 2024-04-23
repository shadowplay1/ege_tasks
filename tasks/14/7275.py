# zxyx8 + xy517 = wzx62
# ^^^^^   ^^^^^   ^^^^^
# 43210   43210   43210

for system in range(9, 100):
    for x in range(system):
        for y in range(system):
            for z in range(system):
                for w in range(system):
                    s1 = (z * system  ** 4) + (x * system ** 3) + (y * system ** 2) + (x * system ** 1) + 8
                    s2 = (x * system ** 4) + (y * system ** 3) + (5 * system ** 2) + (1 * system ** 1) + 7
                    s3 = (w * system ** 4) + (z * system ** 3) + (x * system ** 2) + (6 * system ** 1) + 2

                    sum_ = s1 + s2

                    if sum_ == s3:
                        num = f'{x}{y}{z}{w}'
                        result = (x * system ** 3) + (y * system ** 2) + (z * system ** 1) + w
                        
                        print(result) # 10877
