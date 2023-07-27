'''
# 학생/ 교수 정보를 나타내기 어려움
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk()

p1 = Person('박교수', 59)
p1.talk()

# 상속 클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self): # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')

        
class Professor(Person):
    def __init__(self, name, age,department):
        # Person.__init__(self, name,age) # 부모 클래스에서 name과 age에 관한 메세드 불러오기
        super().__init__(name, age) # 부모 클래스에서 name과 age에 관한 메세드 불러오기
        self.department = department

        
class Student(Person):
    def __init__(self, name, age, gpa):
        # Person.__init__(self, name,age) # 부모 클래스에서 name과 age에 관한 메세드 불러오기
        super().__init__(name, age) # 부모 클래스에서 name과 age에 관한 메세드 불러오기
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk() # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 반갑습니다. 김학생입니다.

# 문제점 1. 유연함이 떨어지는 코드가 됨. (부모 클래스명이 바뀌면 자식 클래스의 클래스명도 바꿔서 작성)


class Person:
    gene = 'XYZ'
    def __init__(self, name):
        self.name = name
        
    def greeing(self): # 메서드 재사용
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'
    
    def __init__(self, name): # 파이썬 정식에 따르면 각각 하위 클래스에도 재정의 해주는게 맞음
        super().__init__(name)
    
    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'
    
    def __init__(self, name): # 파이썬 정식에 따르면 각각 하위 클래스에도 재정의 해주는게 맞음
        super().__init__(name)
    
    # def __init__(self, name, age): 
    #     super().__init__(name)
    #     self.age = age

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Mom, Dad):
    # dad_gene = Dad.gene
    # Dad.__init__(self, name, age)

    def __init__(self, name): # 파이썬 정식에 따르면 각각 하위 클래스에도 재정의 해주는게 맞음
        super().__init__(name)

    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    

baby1 = FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # XX를 Mon 먼저 상속받아서 부모 클래스의 gene = 'XX'를 받아옴.
# print(baby1.dad_gene) # XY

print(FirstChild.mro())
# [<class '__main__.FirstChild'>, <class '__main__.Mom'>, <class '__main__.Dad'>, <class '__main__.Person'>, <class 'object'>]
# -> 방향으로 탐색해 나아감

# 복수 예외 처리 연습
try:
    num = int(input('100으로 나눌 값을 입력해 : '))
    print(100 / num)
except ValueError:
    print('숫자를 입력하라고')
except ZeroDivisionError:
    print('왜 0을 입력하는거야??')
# except(ValueError, ZeroDivisionError):
#     print('제대로 입력해')
except:
    print('에러가 발생했어')

try:
    num = int(input('100으로 나눌 값을 입력해 : '))
    print(100 / num)
except BaseException:
    print('숫자를 입력하라고')
except ZeroDivisionError:
    print('왜 0을 입력하는거야??')
except:
    print('에러가 발생했어')

'''
class Person:
    number = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Person.number += 1
        type(self).number += 1

    def __str__(self):
        return self.name
    
    @classmethod
    def getNumber(cls):
        return cls.number
        


class Professor(Person):
    # # a = super()
    # def __init__(self, name, age):
    #     super().__init__(name, age)
    
    pass

class Student(Person):
    def __init__(self, name, age, no):
        super().__init__(name, age)
        # Person.__init__(self, name, age)
        self.no = no
    

    def __str__(self):
        return f'{self.no}_{self.name}'




s1 = Student('김씨', 20, 's1000') # self = s1
s2 = Student('이씨', 22, 's1001') # self = s2

p1 = Professor('박씨', 40)

print(s1, s2, p1)
print(Person.getNumber())
print(Professor.getNumber())
print(Student.getNumber())
print(s1.getNumber())