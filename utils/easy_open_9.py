# открываем файл
f=open('9.csv').readlines()

# переводим из строки с "\r" и "\t" в массив чисел
arr = [list(map(int, x.split())) for x in f]
