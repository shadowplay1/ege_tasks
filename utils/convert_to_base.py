# перевод любого десятичного числа в указанную систему счисления
def convert_to_base(n: int, base: int) -> str:
    alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    res = ''

    while n > 0:
        res = alf[n % base] + res
        n //= base

    return res
