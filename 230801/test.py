T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for tc in range(1,11):  # 테스트 케이스가 10개라고 했음
    # 모든 빌딩에 대해서 조망권이 있는 세대수 계산해서 더하기
    N = int(input())
    buildings = list(map(int,input().split()))
    result = 0    #누적합을 구해야 하기 때문에... 초기값은 0
    for i in range(2,N-2): # i : 빌딩번호
        # i번 건물의 높이 : A
        A = buildings[i]
        # 주변 네개 건물 중 가장 높은 건물 높이 B
        neighbors = [buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2]]
        max_v = neighbors[0]
        for j in range(4):
            if max_v < neighbors[j]:
                max_v = neighbors[j]
        B = max_v
        # result += A - B if A > B else 0
        if A > B:   # 조망권이 있는 경우에만 더하기
            result += A - B

    print(f'#{tc} {result}')

