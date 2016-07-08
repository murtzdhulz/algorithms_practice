def knapsack(B,val,wts):
    n=len(wts)
    T=[[0]*(B+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for b in range(1,B+1):
            if wts[i-1]<=b:
                T[i][b]=max(T[i-1][b],val[i-1]+T[i-1][b-wts[i-1]])
            else:
                T[i][b]=T[i-1][b]
    return T[n][B]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print knapsack(W , val, wt)