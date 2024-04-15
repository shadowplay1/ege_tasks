from functools import lru_cache

# системам ходов. изменения могут быть только в h и в return .
def move(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 4, b), (a, b * 4)

# алгоритм игры
# в может поменяться строчка if sum(h) ... т.к могут быть 1 или 2 кучи
@lru_cache(None)
def game(h):
    a, b = h

    if sum(h) >= n: # n - количество камней, при которых игра завершается
        return 'end'

    if any(game(m) == 'W' for m in move(h)):
        return 'P1'

    if all(game(m) == 'P1' for m in move(h)):
        return 'V1'

    if any(game(m) == 'V1' for m in move(h)):
        return 'P2'

    if all(game(m) == 'P1' or game(m) == 'P2' for m in move(h)):
        return 'V2'

# цикл вывода данных
for s in range(1, 94):
    h = (6, s)

    if game(h) is not None and game(h) != 'P1':
        print(s, game(h))
