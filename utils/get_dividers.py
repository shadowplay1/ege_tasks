def get_dividers(n) -> list[int]:
    dividers = []

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            dividers.append(i)

    return dividers