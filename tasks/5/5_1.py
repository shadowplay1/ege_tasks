arr=[]
for i in range(1,100000):
    bin_i = bin(i)[2:]
    if i%3==0:
        bin_i += bin_i[-3:]
    else:
        bin_i += bin((int(bin_i,2)%3)*3)[2:]
    if int(bin_i,2)>151:
        arr.append(int(bin_i,2))
print(min(arr))

# made by isp