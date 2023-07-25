# hw_6_2.py

# 아래 함수를 수정하시오.
# 방법1.
def remove_duplicates_to_set(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return set(new_list)

# 방법2.
# def remove_duplicates_to_set(lst):
#     return set(lst)
result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
