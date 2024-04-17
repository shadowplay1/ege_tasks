f=open('27/27A_7603.txt').readlines()
arr=[int(x)for x in f]
n=arr[0]
k=arr[1]
print(n,k)
max_sum=0
for i in range(len(arr)):
    for j in range(i+k,len(arr)):
        max_sum=max(max_sum,arr[i]+ arr[j])
print(max_sum)
# 7603
