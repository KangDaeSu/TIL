

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    value = list(map(int, input()))
    # print(N,value)
    counts = [0] * 10
    for d in value:
        counts = counts[d] #[0,0,0,0,1,0,1,1,0,2]
        print(counts)
    #counts 배열에서 최대값과 index를 구한다.

