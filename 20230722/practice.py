'''
my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]

# 인덱싱
print(len(my_list)) # 5
print(my_list[4][-1]) # !!!
print(my_list[-1][1][0]) # w


my_list2 = [1, 2, 3]
my_list2[0] = 100

print(my_list2)
------------------------
my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1]) # a

# 슬라이싱
print(my_tuple[2:4]) # (3, 'b')
print(my_tuple[:3]) # (1, 'a', 3)
print(my_tuple[3:]) # ('b', 5)
print(my_tuple[0:5:2]) # (1, 3, 5)
print(my_tuple[::-1]) # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_tuple)) # 5

my_tuple = (1, 'a', 3, 'b', 5)

# TypeError : 'tuple' object does not support item assignment
my_tuple[1] = 'z'
--------------------------

x, y = (10, 20)

print(x) # 10
print(y) # 20

# 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
x, y = 10, 20
------------------------------

my_range_1 = range(5)
my_range_2 = range(1, 10)

print(my_range_1) # range(0, 5)
print(my_range_2) # range(1, 10)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1)) # [0, 1, 2, 3, 4]
print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
------------------------------------------------------

my_dict_1 = {}
my_dict_2 = {'key' : 'value'}
my_dict_3 = {'apple' : 12, 'list' : [1, 2, 3]}

print(my_dict_1) # {}
print(my_dict_2) # {'key': 'value"}
print(my_dict_3) # {'apple': 12, 'list': [1, 2, 3]}

my_dict = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict['apple']) # 12
print(my_dict['list']) # [1, 2, 3]

#값 변경
my_dict['apple'] = 100
print(my_dict) # {'apple': 100, 'list': [1, 2, 3]}
----------------------------------------------------

my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1) # set()
print(my_set_2) # {1, 2, 3}
print(my_set_3) # {1}


my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2) # {1, 2}

#교집합
print(my_set_1 & my_set_2) # {3}
--------------------------------------------------

variable = None
print(variable) # None
--------------------------------------------------

bool_1 = True
bool_2 = False

print(bool_1) # True
print(bool_2) # False
print(3 > 1) # True
print('3' != 3) # True
------------------------------------------------

my_str = 'hello'
# TypeError : 'str' object does not support item assignmet
my_str[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100

print(my_list) # [100, 2, 3]
'''

print(3 + 5.0) # 8.0
print(True + 3) # 4
print(True + False) # 1

print(int('1')) # 1
print(str(1) + '등') # 1등
print(float('3.5')) # 3.5
print(int(3.5)) # 3

#ValueError: invalid literal for int() with base 10: '3.5'
print(int('3.5'))