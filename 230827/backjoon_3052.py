nums = [int(input()) for _ in range(10)]

lst = []
for i in range(10):
    v = nums[i] % 42
    lst.append(v)
result = set(lst)
print(len(result))