def func3():
    n = 3
    print(3)
    return

def func2():
    n = 2
    func3()
    print(2)
    return

def func1():
    n = 1
    func2()
    print(1)
    return

n = 0
func1()

# 팩토리얼 재귀
def factorial(n):
    if n == 1:
        return 1
    result = n * factorial(n-1)
    return result

factorial(5)

# 피보나치
def fib(n):
    if memo[n] != -1:   # 이미 알고 있는지 :
         return memo[n] # 알고 있는 값

    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # if n <= 1:
    #     memo[n] = n
    #     return n

    v1 = fib(n-1)
    v2 = fib(n-2)
    memo[n] = v1 + v2 # memo 리스트에 값 저장

    return memo[n]

N = 5
memo = [-1] * (N+1) # Memoization 사용을 위해 빈 리스트 지정
memo[0] = 0 # 0 값을 미리 지정
memo[1] = 1 # 1 값을 미리 지정
print(fib(5))