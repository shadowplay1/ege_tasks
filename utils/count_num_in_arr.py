def find_number_repeated_three_times(nums):
    count = {}
    # Подсчет частоты каждого элемента
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Поиск числа, повторяющегося ровно три раза
    for num, freq in count.items():
        if freq == 3:
            return num

    return None 