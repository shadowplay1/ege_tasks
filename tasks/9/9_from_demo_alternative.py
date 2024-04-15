# открываем файл, создаём счётчик
f = open('9_2024.csv').readlines()
count = 0

# проходимся по всем строкам файла
for i in f:
    # конвертируем строку в массив с числами
    s = list(map(int, i.split(';')))

    # заводим список повторяющихся чисел
    repeat = [x for x in s if s.count(x) == 2]

    # если два числа повторяются 2 раза:
    if len(repeat) == 4:
        if (sum(repeat) / len(repeat)) < (sum(s) / len(s)):
            count += 1

# выводим результат
print(count)
