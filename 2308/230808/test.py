# for _ in range(10):
#     T = int(input())
#     word = input()
#     data = input()
#     ans = 0
#     for i in range(len(data)-len(word)):
#         if data[i:i+len(word)]== word:
#             ans += 1
#     print(f'#{tc} {ans}')

# 고지식한 알고리즘(Brute Force)
# t안에서 p가 존재하면 위치를 return, 못찾으면 -1 return
def brute(t, p):
    N = len(t)
    M = len(p)
    
    tp = 0 # text의 위치
    pp = 0 # patt의 위치
    while tp < N and pp < M:
        if t[tp] == p[pp]:
            tp = tp - pp + 1
            pp = 0
        else:
            tp += 1
            pp += 1
    if pp == M:
        return tp-pp
    else:
        return -1
    

text = 'TTTTAACCA'
patt = 'TTA'
print(brute(text, patt))