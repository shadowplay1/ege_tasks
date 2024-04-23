f = open('9-0.csv').readlines()
# line 1 in table: times

times = f[0].split(',')[1:]
data: list[int] = []

for i in range(len(f[1:])):
    splitted = f[1:][i].split(',')
    row = list(map(float, splitted[1:]))

    try:
        if times[i] in ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00']:
            data.append(row[i])
    except:
        pass

    # for j in row:
        # data.append(j)

sr = sum(data) / len(data)
print(sr - max(data))
