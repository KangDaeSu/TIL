# # 진법 변경 (10진수 -> n진수)
# print(bin(12))
# print(oct(12))
# print(hex(12))

# print(2 / 3)

# print(5 / 3)

# #지수(제곱하는 회수 )표현
# print(314e-2)
# print(314e2)

# #f-string
# bugs = 'rpaches'
# counts = 100
# area = ('living room')
# print(f'Debugging {bugs} {counts} {area}')

# #f-string 응용
# greeting = 'hi'
# print(f'{greeting:^10}') #          hi
# print(f'{greeting:>10}') #               hi
# print(f'{3.141592:.4f}')

# x = 10
# y = x

# x = 20
# print(x)
# print(y)

# s = 'apple'
# l = list(s)
# print(l, type(l))

# ss = set(s)
# print(ss, type(ss))

# d = {'a' : 1, 'b' : 3, 'c' : 4} 
# l = list(d)
# print(l, type(l))

# s = set(d)
# print(s, type(s))

# l = []
# l = list[]
# s = ' '
# d = dict()

# s = set()

# y = 10
# y -= 4
# print(y)

# a = 2
# print( != 2)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a), id(b))
# r1 = a ==b
# r2 = a is b
# print(r1, r2)

# c = a
# print(id(a), id(c))
# print(a == c, a is c)

# a = 0
# if a:
#     print('T')

# vowels = 'aeiou'
# print(('a' and 'b') in vowels)
# print(('b' and 'a') in vowels)
# if '':
#     print('T')
# print(3 and 5)
# print(3 and 0)
# print(0 and 5)
# print(0 and 0)

# print(5 or 3)
# print(3 or 0)
# print(0 or 3)
# print(0 or 0)

# print('Gildong' + 'Hong')

# book = '1'
# total = 10
# guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
# print(guide)
# print(len(book) * total)

# changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
# rental = 3.0
# print(changes)
# print(int(total - rental))


# authors = ['작자 미상', '이항복', '임제', '임제', 
#            '조성기', '조성기', '조성기', '임제', 
#            '허균', '허균', '허균', '임제', '임제', 
#            '임제', '임제', '임제', '임제', '임제', 
#            '임제', '임제', '임제', '박지원', '이항복', 
#            '남영로', '남영로', '남영로', '이항복', '임제', '임제']


# print(list(set(authors)))
import copy
catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'], 
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'], 
    ['황금의 칼날', '비열한 간신', '무명의 영웅'], 
    ['성공의 열쇠', '내면의 변화', '목표의 달성']
]

backup_catalog = copy.deepcopy(catalog)

''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''
catalog[3][0] = '성공을 향한 한 걸음'
catalog[3][1] = '내 삶의 변화'
catalog[3][2] = '목표 달성의 비밀'
print('catalog와 backup_catalog를 비교한 결과')
# 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오. 
print(catalog == backup_catalog)

print('backup_catalog : ')
print(backup_catalog)
print()

print('catalog : ')
print(catalog)