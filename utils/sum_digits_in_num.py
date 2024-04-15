# суть этой строчки в return ....
def sum_of(n: str) -> int:
    # Здесь мы итерируемся по строке и проверяем является ли значение цифрой.
    # Данную строчку можно переписать как retutn sum(int(x) for x in n)
    return sum(int(x) for x in n if x.isdigit())


# made by isp
