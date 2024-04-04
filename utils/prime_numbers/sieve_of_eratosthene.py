def sieve_eratoshen(n):
    if n<=2:return 0
    prime_num = [True]*n
    prime_num[0],prime_num[1] = False,False
    p=2
    while (p**2 < n):
        if prime_num[p] == True:
            for i in range(p**2,n , p):
                prime_num[i]=False
        p+=1
    return (sum(prime_num))

# made by isp