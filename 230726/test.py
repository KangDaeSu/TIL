'''
# 클래스 정의
class Person:
    pass

# 인스턴스 생성
iu = Person()

# 메서드 호출
iu.메서드()

# 속성(변수)접근
iu.attribute


# 클래스 정의
class Person:
    blood_color = 'red'

    # 메서드 => 개발자가 적접 만들지 않음
    def __intit__(self, name): # 생성자 메서드
        self.name = name
    
    def singing(self):
        return f'{self.name}가 노래합니다.'
    
# 인스턴스 생성
singer1 = Person('iu')

# 메서드 호출
print(singer1.singing())
print(singer1.blood_color)
print(singer2.singing)


#인스턴스.메서드()
'abc'.upper()

# 클래스.메서드(인스턴스 자기자신)
upper('abc')
'''