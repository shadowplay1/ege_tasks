# 10100
f=open('txt/17_1.txt').readlines()
max_val_pos = 0
m=[]
k=0
arr=[int(x) for x in f]
for i in arr:
    if i >max_val_pos:
        if str(i)[-2:]=="13":
            max_val_pos = i
# Этот цикл проходит по списку arr и рассматривает каждую тройку.
# Если два из трех чисел в тройке состоят из трех цифр, и сумма этих троек не превышает max_val_pos, то эта сумма добавляется в список m
for i in range(len(arr)-2):
    if (len([x for x in [arr[i],arr[i+1],arr[i+2]] if len(str(x))==3])==2) and ((arr[i]+arr[i+1]+arr[i+2])<=max_val_pos):
        m.append(arr[i]+arr[i+1]+arr[i+2])
        k+=1


print(max(m),k)


# made by isp