# 재귀 순열

def perm(k):
    # if k == 3:  4P3
    if k == N:
        print(bits)
        for i in range(N):
            pos = bits[i]
            print(numbers[pos], end=' ')
        print()
        return

    for i in range(N):
        if not used[i]:
            bits[k] = i
            used[i] = True
            perm(k+1)
            used[i] = False

N = 4
# 0 1 2
# 0 2 1
# 1 0 2
# 1 2 0
# 2 0 1
# 2 1 0
numbers = [8, 10, 20, 3]

bits = [-1] * N
used = [False] * N
# bits[0] = 0   # 첫번째 고정
# used[0] = True    # 첫번째 고정
perm(0)
