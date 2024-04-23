# 8483
# f=open('27/test_8483.txt').readlines()
f=open('27/27A_8483.txt').readlines()
arr=[int(x) for x in f]
n,k = arr[0] , arr[1]
arr.remove(arr[0])
arr.remove(arr[0])
# print(n,k)
# print(arr)
max_sum=0
for i in range(n):
    for j in range(i+1,n):
        for z in range(j+1,n):
                if arr[i] != arr[z] !=arr[j]:
                     if abs(i - z)>=k and abs(i - j)>=k and abs(z - j)>=k :
                          max_sum = max(max_sum,arr[i] + arr[j] + arr[z])
print(max_sum) 


# made by isp