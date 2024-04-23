f = open('9-0.csv').readlines()

data: list[int] = []

for i in f:
    row = list(map(float, i.split(',')[1:]))
    
    for j in row:
        data.append(j)

print(max(data) - min(data))
