# перевод любого десятичного числа в указанную систему счисления
def convert_to_base(n: int, base: int) -> str:
    converted = ''
    
    while n > 0:
        remainder = n % base
        converted = str(remainder) + converted

        n = n // base

    return converted
