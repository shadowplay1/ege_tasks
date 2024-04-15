# открываем файл
f=open('example.txt').readlines()
# переводим из строки с "\r" и "\t" в массив чисел
arr = [list(map(int, x.split())) for x in f]