# 조건문과 함께 len, sum, min, max 함수 대치
numbers = [2, 5, 7, 10, 6]
#전체길이
# def getLen(numbers):
#     l = 0
#     for n in numbers:
#         l += 1
#     return l

# print(getLen([2, 5, 7, 10, 6]))
# #짝수만
# def getLen(numbers):
#     l = 0
#     for n in numbers:
#         if n % 2 ==0:
#             l += 1
#     return l

# print(getLen([2, 5, 7, 10, 6]))
# chr, ord 활용
# 문자와 숫자사이의 변경
# ord('A') + 2
# print(chr(ord('A') + 2))
# print(chr(ord('a') + 2))
# print(ord('a'))
# print(ord('A'))
# print(ord('0'))


# 이차원 배열
'''
a = [
    [1, 2, 3],
    [3, 4, 5],
    [2, 5, 6],
    [12, 5, 6]
]
# a0 = a[0]
# print(a0[1], a[0][1])
cur_max = 0
for r in range(4):
    s = 0
    for c in range(3):
        # print(a[r][c]) #요소 전체 출력
        s = s + a[r][c]
    print('sum = ', s) # 한줄씩 더한 값 출력
    if cur_max < s:
        cur_max = s
print('max = ', cur_max)
'''

# def getFour(numbers):
#     for r in range(row):
#         for c in range(col):
#             # print(numbers[r][c])
#             if numbers[r][c] == 4:
#                 return r, c


# a = [
#     [1, 2, 3],
#     [3, 2, 5],
#     [2, 5, 6],
#     [12, 5, 4]
# ]
# for c in range(col):
#     for r in range(row):
#         print(a[r][c])
# row = 4
# col = 3
# cur_row, cur_col = getFour(a)

# for i in range(2):
#     cur_col += 1
#     if 더이상 갈 수 없으면:
#     break


# 입력
# r = []
# for _ in range(4):
#     i = list(map(int, input().split()))
#     r.append(i)

# r= - [list(map(int, input().split())) for _ in range(4)]
# s = [1, 1, 1]
# s = [[1] * 3  for _ in range(4)]
# s[0][1] = 100
# print(s)


# 재귀 함수

# def mul(value, cnt):
#     if cnt == 1:
#         return value

#     return value * mul(value, cnt-1)

# print(mul(5, 3))


# def rec(n):
#     if n == 1:
#         return 1
    
#     return rec(n-1) + n

# print(rec(5))

# def fac(n):
#     if n == 1:
#         return 1
#     return n * fac(n-1)

# print(fac(4))

# lst = [2, 3, 6, 9, 10]
# def rec(n):
#     if n == 0:
#         return lst[0]
#     return rec(n-1) + lst[n] 
# print(rec(3))

# def rec(n, cur_sum):

#     return rec(n+1, cur_sum + lst[n])

# print(rec(0, lst[0])) # 위치와 해당 위치에 들어갈 값
'''
def make(str, n):
    if n == 0:
        return str
    return make(str, n-1) + str

print(make('a', 5))

def make1(cnt):
    if cnt == 0:
        return lst[0]
    return make1(cnt-1) + lst[cnt] # o
    # return lst[cnt] + make1(cnt-1) # x

lst = ['h', 'e', 'l', 'l', 'o']


cnt = 0
for c in lst:
    cnt += 1
print(make1(cnt-1))


# 123 => ['1', '2', '3']
print(list(str(123)))
# '123' => [1, 2, 3]
a = '123'

'''


# 시험 성적의 합은?
# def getScore(my_dict): # 참조: my_dict.values(), my_dict.items()
#     a = 0
#     for i in my_dict:
#         print(i, my_dict[i])
#         a += my_dict[i]
#     return a

# my_dict = {
#     '김씨' : 80,
#     '이씨' : 70,
#     '박씨' : 60
# }
# print(getScore(my_dict))


# 70점 이상인 사람의 수는?
# def getScore(my_dict): # 참조: my_dict.values(), my_dict.items()
#     count = 0
#     for i in my_dict:
#         if my_dict[i] >= 70:
#             count += 1

#     return count

# my_dict = {
#     '김씨' : 80,
#     '이씨' : 70,
#     '박씨' : 60
# }

# print(getScore(my_dict))


# 70점 이상 점수의 합은?
# def getScore(my_dict): # 참조: my_dict.values(), my_dict.items()
#     a = 0
#     for i in my_dict:
        
#         if my_dict[i] >= 70:
#             a += my_dict[i]
         
#     return a

# my_dict = {
#     '김씨' : 80,
#     '이씨' : 70,
#     '박씨' : 60
# }

# print(getScore(my_dict))

# 70점 이상 점수의 평균은?

def getScore(my_dict): # 참조: my_dict.values(), my_dict.items()
    a = 0
    count = 0
    for i in my_dict:
        
        if my_dict[i] >= 70:
            a += my_dict[i]
            count += 1
    return a / count

my_dict = {
    '김씨' : 80,
    '이씨' : 70,
    '박씨' : 60
}

print(getScore(my_dict))