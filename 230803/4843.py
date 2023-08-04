import sys
sys.stdin = open("4843.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    for i in range(N):
        maxIdx = i
        if i % 2 ==0 :
            for j in range(i, N):
                if nums[maxIdx] < nums[j]:
                    maxIdx = j
            nums[i], nums[maxIdx] = nums[maxIdx], nums[i]
        else:
            for j in range(i, N):
                if nums[maxIdx] > nums[j]:
                    maxIdx = j
            nums[i], nums[maxIdx] = nums[maxIdx], nums[i]
    result = nums[:10]
        

    print(f'#{tc}', *result)
