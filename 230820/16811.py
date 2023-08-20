# 당근
import sys
sys.stdin = open("16811.txt", "r")

for test_case in range(1, int(input())+1):
    n = int(input())
    carrots = sorted(list(map(int, input().split())))
    result = 100000
    maxlen = n / 2
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if i > maxlen or (j - i) > maxlen or (n - j) > maxlen:
                continue
            if carrots[i-1] == carrots[i] or carrots[j-1] == carrots[j]:
                continue
            result = min(result, max(i, j-i, n-j) - min(i, j-i, n-j))

    if result == 100000:
        result = -1

    print(f"#{test_case} {result}")

    