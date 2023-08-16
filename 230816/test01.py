# 재귀
def f(i, N):
    if i == N:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, N)
        return

N = 3
A = [1, 2, 3]
B = [0] * N
f(0, N)
print(B)

def f(i, N):
    if i == N:
        print(bit, end = ' ')
        for j in range(N):
            if bit[j]:
                print(A[j], end = ' ')
        print()
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)
        return

A = [1, 2, 3]
bit = [0]*3
f(0, 3)

# 재귀1
def f(i, N):
    if i == N:
        print(bit, end = ' ')
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end = ' ')
        print(f' : {s}')
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)
        return

A = [1, 2, 3]
bit = [0]*3
f(0, 3)

# 재귀2
def f(i, N, s): # s : i-1원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end = ' ')
        # s = 0
        # for j in range(N):
        #     if bit[j]:
        #         s += A[j]
        #         print(A[j], end = ' ')
        print(f' : {s}')
        return
    else:
        bit[i] = 1  # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i])
        bit[i] = 0  # 부분집합에 A[i] 빠짐
        f(i+1, N, s)
        return

A = [1, 2, 3]
bit = [0]*3
f(0, 3, 0)

# 재귀를 사용한 백트래킹
def f(i, N, s, t): # s : i-1원소까지 부분집합의 합(포함된 원소의 합), t : 찾으려는 합
    global cnt
    cnt += 1
    if s == t:  # 찾고자 하는 합과 s가 같을 때
        print(bit)
        return
    elif i == N:    # t는 아니지만 남은 원소가 없는 경우
        return
    elif s > t:
        return
    else:
        bit[i] = 1  # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i], t)
        bit[i] = 0  # 부분집합에 A[i] 빠짐
        f(i+1, N, s, t)
        return

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N+1)]
bit = [0]*N
t = 10
cnt = 0
f(0, N, 0, t)

print(cnt)
# 찾고자 하는 결과에 따라 백트래킹과 dfs와 차이가 많이 없을 수 있음
