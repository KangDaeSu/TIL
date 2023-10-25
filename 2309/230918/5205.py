import sys
sys.stdin = open('input.txt', 'r')

def h_par(s, e):
    p = s
    i = s
    j = e
    while i <= j:
        while i <= j and lst[i] <= lst[p]:
            i += 1
        while i <= j and lst[j] >= lst[p]:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[p], lst[j] = lst[j], lst[p]
    return j


def quick_sort(s, e):
    if s >= e:
        return -1

    pivot = h_par(s, e)
    quick_sort(s, pivot-1)
    quick_sort(pivot + 1, e)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    # print(N, lst)


    quick_sort(0, N-1)
    result = lst[N//2]

    print(f'#{tc} {result}')