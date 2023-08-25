import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sumV = nums[i]+nums[j]+nums[k]
            if sumV <= M:
                result = max(result, sumV)
                break
                
print(result)

    
