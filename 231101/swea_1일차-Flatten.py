T = 10
for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for i in range(dump):
        max_high = max(boxes)
        min_high = min(boxes)
        boxes[boxes.index(max_high)] -= 1
        boxes[boxes.index(min_high)] += 1
        if max_high - min_high <= 1:
            break
    max_high = max(boxes)
    min_high = min(boxes)
    print(f'#{tc} {max_high-min_high}')