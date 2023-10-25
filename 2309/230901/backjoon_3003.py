import sys
sys.stdin = open("input.txt", "r")

lst = list(map(int, input().split()))

chess_lst = [1, 1, 2, 2, 2, 8]
for i in range(len(lst)):
    if lst[i] > chess_lst[i]:
        lst[i] = - abs(lst[i] - chess_lst[i])
    elif lst[i] < chess_lst[i]:
        lst[i] = abs(lst[i] - chess_lst[i])
    else:
        lst[i] = 0
print(*lst)