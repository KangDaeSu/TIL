import sys
sys.stdin = open("input.txt", "r")

s = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in lst:
    if i in s:
        s = s.replace(i, '0')

print(len(s))
