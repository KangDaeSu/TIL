'''
def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    
    return f[n]

def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

cnt = 0
print(fibo(30), cnt)

# memo
def fibo(n):
    global cnt
    global memo
    cnt += 1
    if n < 2:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]
N = 30
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 1
cnt = 0
print(fibo(N), cnt)

# DP
def fibo(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

dp = [0] * (100+1)
dp[0] = 0
dp[1] = 1
for i in range(2, 101):
    dp[i] = dp[i-1] + dp[i-2]

print(fibo(100))
'''
