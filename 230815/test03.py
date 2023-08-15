'''
A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)

A = input()
B = '??!'
print(A+B)

A = int(input())
print(A-543)

A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

A = int(input())
B1, B2, B3 = map(int, input())
print(A * B3)
print(A * B2)
print(A * B1)
print(A * ((100*B1)+(10*B2)+B3))

A, B, C = map(int, input().split())
print(A+B+C)

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\__|")

A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')

A = int(input())
if 90 <= A <= 100:
    print('A')
elif 80<= A <90:
    print('B')
elif 70<= A <80:
    print('C')
elif 60<= A <70:
    print('D')
else:
    print('F')

N = int(input())
arr = list(map(int, input().split()))
V = int(input())

cnt = 0
for i in arr:
    if i == V:
        cnt += 1
print(cnt)

N, X = map(int, input().split())
arr = list(map(int, input().split()))

for i in arr:
    if i < X:
        print(i, end = ' ')

N = int(input())
arr = list(map(int, input().split()))

min_num = arr[0]
max_num = arr[0]
for i in arr:
    if i < min_num:
        min_num = i
    elif i > max_num:
        max_num = i
print(f'{min_num} {max_num}')

arr = [int(input()) for _ in range(9)]
max_num = arr[0]
for i in range(len(arr)):
    if arr[i] > max_num:
        max_num = arr[i]
result = arr.index(max_num)+1
print(max_num, result, sep = '\n')

N, M = map(int, input().split())

basket = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        basket[n] = k

for i in range(1, N+1):
    print(basket[i], end = ' ')

N, M = map(int, input().split())
lst = [0] * (N+1)
for _ in range(M):
    s, e, N = map(int, input().split())
    for i in range(s, e+1):
        lst[i] = N

print(*lst[1:])

import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
basket = [k for k in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)
'''
