N = int(input())
nums = [0] + list(map(int, input().split()))
lst = []
for i in range(1, N+1):
    v = len(lst) - nums[i]
    lst.insert(v, i)
print(*lst)