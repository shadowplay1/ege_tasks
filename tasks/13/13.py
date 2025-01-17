import ipaddress


# если первое число в айпи адресе меньше 128,
# то двоичная запись через bin потеряет нулевые двоичные разряды (незначащие нули)

# для решения этой проблемы можно использовать:
# - f-строку: f'{ip:b}'
# - функцию format: format(ip, 'b')

# ^ ip не должен быть int, иначе незначащие нули не будут дописаны

net = ipaddress.ip_network('102.168.32.160/255.255.255.240')
count = 0

for ip in net:
    b = bin(int(ip))[2:]
    formatted = f'{ip:b}' # or format(ip, 'b')
    
    # задача: найти количество айпи-адресов с чётным количетсвом единиц
    if b.count('1') % 2 == 0:
        count += 1


# [!] если в задаче спрашивается какое-либо количество *компьютеров/хостов*,
# то нужно *всегда* вычитать 2 из счётчика, чтобы исключить подсчёт
# адреса самой сети и широковещательного адреса

# если нужно узнать какое-либо количество *айпи-адресов*, то
# вычитать ничего не нужно

print(count)
