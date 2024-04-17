# f=open('27/test_7878.txt').readlines()
f=open('27/27A_7878.txt').readlines()
arr=[int(x) for x in f]
n,k = arr[0] , arr[1]
# print(n,k)
arr.remove(arr[0])
arr.remove(arr[0])
# print(arr)
# arr.sort()
min_=1000000000000
for i in range(n):
    for j in range(n):
        if (arr[i] * arr[j])%157==0 and abs(j-i)>=k:
            min_=min(min_,arr[i] * arr[j])
print(min_)