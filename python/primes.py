def print_primes(n):
    prime_arr = [True]*(n+1)
    res=[]

    i=2
    # make the sieve
    while i*i<=n:
        if prime_arr[i]:
            for j in range(i*i,n+1,i):
                prime_arr[j]=False
        i+=1

    for i in range(2,len(prime_arr)):
        if prime_arr[i]:
            res.append(i)

    return res

print print_primes(11)
print print_primes(43)