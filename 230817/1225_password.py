import sys
sys.stdin = open("1225_password.txt", "r")
def password(s):
    while True:
        for i in range(1, 6):
            v = s.pop(0) - i
            if v <= 0:
                v = 0
                s.append(v)
                return s
            s.append(v)

T = 10
for _ in range(1, T+1):
    tc = int(input())
    lst = list(map(int, input().split()))

    Q = lst


    result = password(Q)
    print(f'#{tc}', *result)