# ws_5_2.py

# 아래 함수를 수정하시오.
# def remove_duplicates(original):
#     new_lst = []
#     for i in original:
#         if i not in new_lst:
#             new_lst.append(i)
    

#     return new_lst

# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

# 방법 1 set 이용

# def remove_duplicates(original):
#     new_lst = list(set(original))
#     return new_lst
# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

# 방법 2-1 set을 이용하지 않고 (반복문)
# def remove_duplicates(original):
#     new_lst = []
#     for i in original:
#         if i not in new_lst:
#             new_lst.append(i)
    

#     return new_lst

# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

# 방법 2-2 set을 이용하지 않고 (dictionary)
def remove_duplicates(original):
    new_dict = {}
    for i in original:
        
        if i in new_dict:
            new_dict[i] +=1
        else:
            new_dict[i] = 1
    return new_dict

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(list(result.keys()))
