# 자기방으로 돌아가기

# 짝수인 복도 번호 //2, (홀수인 복도 번호+1) //2
# 복도번호 = (방번호 + 방번호%2)//2
import sys
sys.stdin = open("4408.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 학생 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * 201 # 방사이 공간을 지나는 사람 수
    for a, b in arr:    # a <= b라는 보장이 없음에 주의
        a = (a + a%2) // 2
        b = (b + b%2) // 2
        for i in range(min(a, b), max(a, b)+1):
            cnt[i]  += 1
    
    print(f'#{tc} {max(cnt)}')