f=open('txt/9_7674.txt').readlines()
arr=[list(map(int,x.split())) for x in f ]
k=0
# print(arr)
# есть 3 числа, которые не повторяются, а среднее значение неповторяющихся чисел, меньше среднего значения повторяющихся чисел
for i in range(len(arr)): 
    c=[x for x in arr[i] if arr[i].count(x)==1]
    m=[x for x in arr[i] if arr[i].count(x)==2]
    if len(c) >0 and len(m) >0: 
        if (sum(c)/len(c)) < (sum(m)/len(m)):
            k+=1
print(k)
# 7674