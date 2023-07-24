# main.py

# 아래 함수를 수정하시오.
# 방법 1.
# def count_character(main,chr): #str : 문자열, chr : 문자 하나
#     new_list = main.lower()
#     new = chr.lower()
#     result = list(new_list).count(chr)
#     return result

# result = count_character("Hello, World!", "o")
# print(result) # 2

# 방법 2.
def count_character(main,chr):
    result = main.count(chr)
    return result
result = count_character("Hello, World!", "o")
print(result) # 2