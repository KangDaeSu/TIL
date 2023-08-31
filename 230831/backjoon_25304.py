X = int(input())
N = int(input())

sumV = 0
for _ in range(N):
    a, b = map(int, input().split())
    sumV += (a*b)

if sumV == X:
    print('Yes')
else:
    print('No')