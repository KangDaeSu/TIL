# ws_5_5.py

# 아래 함수를 수정하시오.
# 방법 1.
def even_elements(numbers):
    result = []
    while len(numbers) > 0: # = while numbers:
        n = numbers.pop(0)
        if n % 2 == 0:
            result.append(n)
            # result.extend([n]) # 들어갈 리스트 요소를 []로 감싸줘야 함.
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

# 방법 2. 
# def even_elements(numbers):
#     result = []
#     for n in numbers:
#         if n % 2 == 0:
#             result.append(n)
#     return result
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)

# !!! 쓰지 말 것
# for idx in range(N):
#     print(idx)
#     numbers.pop(idx)