T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    count = [0] * (max(arr) + 1)
    for i in arr:
        count[i] += 1

    idx = 0
    max_num = 0
    for i in range(len(count)):
        if idx <= count[i]:
            idx = count[i]
            max_num = i
    print(f'#{tc} {max_num} {idx}')