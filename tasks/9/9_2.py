f=open('txt/9_2.txt').readlines()
arr=[list(map(int,x.split()))for x in f]
k=0
def ccount(nums):
    counter=0
    dict_={}
    for num in nums:
        if num in dict_:
            dict_[num]+=1
        else:
            dict_[num]=1
    for num,c in dict_.items():
        if c==2:
            counter+=1
            if counter==2:
                return True
    return False
for i in range(len(arr)):
    m=[x for x in arr[i] if arr[i].count(x)==2]
    if len(m)>0 and ccount(arr[i]):
        if (sum(arr[i])/len(arr[i])) > (sum(m)/len(m)):
            k+=1
print(k)


# made by isp