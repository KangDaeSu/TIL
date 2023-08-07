import sys
sys.stdin = open("1221.txt", "r")

T = int(input())
for tc in range(1, T+1):
    _, N = list(map(str, input().split()))
    arr = list(map(str, input().split()))

    num = [['ZRO', 0], ['ONE', 0], ['TWO', 0], ['THR', 0], ['FOR', 0],
           ['FIV', 0], ['SIX', 0], ['SVN', 0], ['EGT', 0], ['NIN', 0]]

    cnt = [0]*len(arr)

    for i in arr:
        for j in range(10):
            if num[j][0] == i:
                num[j][1] += 1

    idx = 0
    for k in range(10):
        for _ in range(int(num[k][1])):
            cnt[idx] = num[k][0]
            idx += 1
    print(f'#{tc}')
    print(*cnt)

