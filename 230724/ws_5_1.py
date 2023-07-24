# ws_5_1.py

# 아래 함수를 수정하시오.
def reverse_string(string):
    new_string = reversed(string)
    result = ''.join(new_string)
    return result
# 1. reversed 사용
#     new_string = reversed(string)
#     return ''.join(new_string)

# 2. 슬라이스
# return original[::-1]

# 3. 반복문
# new_string = ''
# for c in original:
#     new_string = c + new_string
# return new_string

# 4. reverse 사용
# lst = list(original)
# lst.reverse()
# return ''.join(lst)
result = reverse_string("Hello, World!")
print(result)

# 참조 문자열을 리스트로 바꾸기 list()
# 리스트(반복개체)를 문자열로 바꾸기 ''.join()