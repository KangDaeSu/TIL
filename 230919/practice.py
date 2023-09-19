'''
# 부분 집합

def subset(k):
    if k == N:
        # print(result)
        sumV = 0
        for i in range(N):
            if result[i]:
                sumV += lst[i]
        #         print(lst[i], end = ' ')
        # print(sumV)
        if sumV == 10:
            for i in range(N):
                if result[i]:
                    print(lst[i], end = ' ')
            print()
        return
    

    # for i in [0, 1]:
    #     result[k] = i
    #     subset(k+1)

    result[k] = 0
    subset(k+1)
    result[k] = 1
    subset(k+1)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
result = [-1] * N
# subset(0)

# 부분집합 - 백트래킹
def subset2(k, cursum):
    if cursum > 10: # 가지치기 조건
        return
    
    if k == N:
        if cursum == 10:
            for i in range(N):
                if result[i]:
                    print(lst[i], end =' ')
            print()
        return  # 리턴 위치 조심

    result[k] = 0
    subset2(k + 1, cursum)
    result[k] = 1
    subset2(k + 1, cursum+lst[k])


subset2(0, 0)
'''

'''
# 순열

def per(k):
    if k == N:
        print(result)
        for i in range(N):
            pos = result[i]
            print(lst[pos], end = ' ')
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            per(k+1)
            visited[i] = False

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 3
result = [-1] * N
visited = [False] * N
per(0)
'''

'''
# 조합

def comb(k, s):
    if k == K:
        print(result)
        return
    
    for i in range(s, N-K+1+k):
        result[k] = i
        comb(k+1, i+1)




lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 4
K = 3
result = [-1] * K
visited = [False] * N

comb(0, 0)
'''