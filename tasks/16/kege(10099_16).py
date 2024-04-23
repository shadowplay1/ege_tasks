# 10099
#в данном задание используются базовые библиотеки для обработки рекурсии 
 
import sys
from functools import lru_cache
sys.setrecursionlimit(99999999)
@lru_cache(None)
def f(n):
    if n>2024:
        return n
    return n*f(n+1)
print(f(2022)/f(2024))

# made by isp