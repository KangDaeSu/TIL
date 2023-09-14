import sys
input = sys.stdin.readline

N = int(input())
num_lst = []
for _ in range(N):
    num_lst.append(int(input()))

my_num = 1
ST = []
res = ''
for i in range(N):
    if my_num <= num_lst[i]:
        while my_num <= num_lst[i]:
            ST.append(my_num)
            my_num += 1
            res += '+\n'
            if my_num == num_lst:
                break
        ST.pop()
        res += '-\n'
    elif my_num > num_lst[i]:
        v = ST.pop()
        res += '-\n'
        if v != num_lst[i]:
            print('NO')
            res = False
            break
if res:
    print(res)