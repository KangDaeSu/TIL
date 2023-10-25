import sys
sys.stdin = open('input.txt','r')

def order(s):
    if '1' in s:
        ST.append(int(s[1]))
    elif '2' in s:
        if ST:
            v = ST.pop()
            print(v)
        else:
            print(-1)
    elif '3' in s:
        l = len(ST)
        print(l)
    elif '4' in s:
        if not ST:
            print(1)
        else:
            print(0)
    elif '5' in s:
        if ST:
            v = ST[-1]
            print(v)
        else:
            print(-1)


N = int(input())
ST = []
for _ in range(N):
    s = list(input().split())
    order(s)

