T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    bus_stop = [i for i in range(N+1)]
    my_pos = 0
    cnt = 0

    flag = True
    while flag:
        for i in range(K, 0, -1):
            if my_pos + i < N:
                if bus_stop[my_pos + i] in lst:
                    cnt += 1
                    my_pos = my_pos + i
                    break
            else:
                flag = False
                break
        else:
            flag = False
            cnt = 0

    print(f'#{tc} {cnt}')