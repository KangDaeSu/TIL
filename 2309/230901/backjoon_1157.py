import sys
sys.stdin = open("input.txt", "r")

s = input()
s = s.upper()
s_lst = list(set(s))

cnt = []
for i in s_lst:
    count = s.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(s_lst[(cnt.index(max(cnt)))])
