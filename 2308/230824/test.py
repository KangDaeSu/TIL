# N : 사람수, M : 시간, K : 붕어빵 수 

T = int(input())
for tc in range(1, T+1):
    person, t, k = map(int, input().split())
    sec = list(map(int, input()))