import ipaddress

net = ipaddress.ip_network('117.32.0.0/255.224.0.0').hosts()
count = 0

for ip in net:
    # for python <3.10:

    # ip = '0' * (32 - len(bin(int(item))[2:])) + bin(int(item))[2:]
    # a = ip[:8]
    # b = ip[8:16]
    # c = ip[16:24]
    # d = ip[24]

    a = f'{ip:b}'[:8]
    b = f'{ip:b}'[8:16]
    c = f'{ip:b}'[16:24]
    d = f'{ip:b}'[24:]
    
    comparison_a = (a == b) or (a == c) or (a == d)
    comparison_b = (b == a) or (b == c) or (b == d)
    comparison_c = (c == b) or (c == a) or (c == d)

    if comparison_a or comparison_b or comparison_c:
        count += 1

print(count)
