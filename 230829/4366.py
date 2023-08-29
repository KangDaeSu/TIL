import sys
sys.stdin = open("4366.txt", "r")




T = int(input())
for tc in range(1, T+1):
    B1 = list(input())    # 2진수 입력  ['1', '0', '1', '0']
    T1 = list(input())    # 3진수 입력  ['2', '1', '2']
    s1 = len(B1)
    s2 = len(T1)

    res1 = []
    for i in range(s1):
        tmp = [-1] * s1  # [-1, -1, -1, -1]
        tmp[i] = str((int(B1[i])+1)%2)
        for j in range(s1):
            if tmp[j] == -1:
                tmp[j] = B1[j]
        res1.append(''.join(tmp))

    res2 = []
    for i in range(s2):
        tmp = [-1] * s2  # [-1, -1, -1]
        tmp[i] = str((int(T1[i])+1)%3)  # 각 자리수를 바꿔서 저장
        for j in range(s2):
            if tmp[j] == -1:    # 바꾼 자리를 제외한 나머지는 그대로 받아옴
                tmp[j] = T1[j]
        res2.append(''.join(tmp))

    for i in range(s2):
        tmp = [-1] * s2  # [-1, -1, -1]
        tmp[i] = str((int(T1[i])+2)%3)
        for j in range(s2):
            if tmp[j] == -1:
                tmp[j] = T1[j]
        res2.append(''.join(tmp))

    final1 = []
    for res in res1:    # 2진수의 리스트를 10진수의 값으로 바꿈
        k = 1
        curr_sum = 0
        for i in range(s1):
            curr_sum += int(res[-1-i]) * k
            k *= 2
        final1.append(curr_sum)

    final2 = []
    for res in res2:    # 3진수의 리스트를 10진수의 값으로 바꿈
        k = 1
        curr_sum = 0
        for i in range(s2):
            curr_sum += int(res[-1-i]) * k
            k *= 3
        final2.append(curr_sum)
    
    for fi1 in final1:
        if fi1 in final2:
            break
    
    print(f'#{tc} {fi1}')