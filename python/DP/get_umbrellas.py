def get_umbrellas(n, p):
    dp = [1001]*(n+1)
    dp[0] = 0
    for i in xrange(n+1):
        for item in p:
            if item<=i and dp[i-item]!=1001:
                dp[i] = min(dp[i], dp[i-item]+1)
    return dp[n] if dp[n]!=1001 else -1

# print get_umbrellas(4,[4,1,2])