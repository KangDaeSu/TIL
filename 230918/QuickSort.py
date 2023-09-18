# 퀵 정렬(quick_sort)

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


# def l_par(s, e):
#     p = e
#     i = s - 1
#     for j in range(s, e):
#         if lst[j] <= lst[p]:
#             i += 1
#             lst[i], lst[j] = lst[j], lst[i]
#     lst[i+1], lst[p] = lst[p], lst[i+1]
#     return i + 1


def quick_sort(s, e):
    if s >= e:
        return -1
    
    pivot = h_par(s, e)
    quick_sort(s, pivot-1)
    quick_sort(pivot+1, e)

lst = [3, 2, 4, 6, 9, 1, 8, 7, 5]
N = len(lst)
quick_sort(0, N-1)
print(lst)