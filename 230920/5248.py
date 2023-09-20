import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    parent[y] = x


T = int(input())
# T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    parent = [i for i in range(N+1)]
    # print(parent)
    for j in range(0, len(lst), 2):
        union(lst[j], lst[j+1])

    res = set()
    for k in range(1, N+1):
        res.add(find_set(k))
    # print(len(res))
    print(f'#{tc} {len(res)}')