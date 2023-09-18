# 병합정렬(merge sort)

def merge(l, r):
    result = []
    lp = rp = 0

    while lp < len(l) and rp < len(r) :
        if l[lp] < r[rp]:
            result.append(l[lp])
            lp += 1
        else:
            result.append(r[rp])
            rp += 1

    result += l[lp:]
    result += r[rp:]

    return result

# lst를 정렬 한 후 결과를 return
def merge_sort(lst):
    N = len(lst)

    if N == 1:
        return lst



    m = N // 2

    # 왼쪽을 merge_sort 이용해서 잘 정렬
    # [2, 10, 30, 69]
    left_lst = merge_sort(lst[:m])
    # 오른쪽을 merge_sort 이용해서 잘 정렬
    # [8, 16, 22, 31]
    right_lst = merge_sort(lst[m:])
    # result = merge(left_lst, right_lst)
    
    return merge(left_lst, right_lst)

lst = [69, 10, 30, 2, 16, 8, 31, 22]
result = merge_sort(lst)
print(result)