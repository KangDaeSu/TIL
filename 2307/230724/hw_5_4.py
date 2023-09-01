# main.py

# 아래 함수를 수정하시오.
# def find_min_max(original):
#     return min(original), max(original)

# result = find_min_max([3, 1, 7, 2, 5])
# print(result) # (1, 7)

def find_min_max(original):
    min = original[0]
    max = original[0]
    for i in original:
        if i < min:
            min = i
        elif i > max:
            max = i
    return min, max

        

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)