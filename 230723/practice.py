'''
# 클래스와 객체
print(help)(str)

------------

# 클래스 정의
class Person:
    pass

# 인스턴스 생성
iu = Person()

# 메서드 호출
iu.메서드()

# 속성(변수) 접근
iu.attribute

------------
'''

class Person():
    blood_color = 'red'

    def __init__(self, name):
        self.name = name
    
    def singing(self):
        return f'{self.name}가 노래합니다.'



# 인스턴스 생성
singer1 = Person('iu')

# 메서드 호출
print(singer1.singing()) # iu가 노래합니다.

# 속성(변수) 접근
print(singer1.blood_color) # red
