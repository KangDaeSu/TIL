N = int(input())

cnt = N // 4
# result = ('long ' * cnt) + 'int'
# print(result)

result = 'int'
for i in range(cnt):
    result = 'long ' + result
print(result)