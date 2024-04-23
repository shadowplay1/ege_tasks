import string

data = open('24.txt').readline()
dict = {}

a = string.ascii_letters[26:] + string.digits

for i in a:
    dict[i] = 0

for i in dict.keys():
    local = 0

    for j in range(len(data) - 1):
        if data[j] == data[j + 1]:
            local += 1
    else:
        dict[i] = max(dict[i], local)
        local = 1

max_val = max(dict.values())
f_d = {k: v for k, v in dict.items() if v == max_val}

print(*f_d, sep='\n')
