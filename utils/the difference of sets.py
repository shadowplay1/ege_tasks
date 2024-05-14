def set_difference(set_a, set_b):
    set_a = set(set_a)
    set_b = set(set_b)
    diff = set_a - set_b
    return list(diff)
set_a = [1,2,3]
set_b=[3,4,5]
# result 3