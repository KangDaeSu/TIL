arr = [list(map(str, input())) for _ in range(5)]

s = 0
for i in range(5):
    s = max(s, len(arr[i]))

res = ''
for c in range(s):
    for r in range(5):
        if len(arr[r]) >= c+1:
            res += arr[r][c]
print(res)
