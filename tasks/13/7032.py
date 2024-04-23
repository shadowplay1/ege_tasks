import ipaddress

net = ipaddress.ip_network('90.65.32.0/255.255.224.0')
c = 0

for ip in net:
    b = f'{ip:b}'

    if b.count('0') == b.count('1'):
        c += 1

print(c)
