import sys
sys.stdin = open("input.txt", "r")

s = list(input())
s_lst = []
for i in range(len(s)-1, -1, -1):
    s_lst.append(s[i])

if s == s_lst:
    print('1')
else:
    print('0')