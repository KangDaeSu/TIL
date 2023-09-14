import sys
sys.stdin = open('input.txt','r')

k = int(input())
ST = []
for _ in range(k):
    n = int(input())
    if n != 0:
        ST.append(n)
    elif n == 0:
        ST.pop()
res = sum(ST)
print(res)