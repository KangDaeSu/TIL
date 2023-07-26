# ws_7_1.py

# 아래 클래스를 수정하시오.
class Shape:
    width = 0
    height = 0
    def __init__(self, width, height): # 초기화 메서드
        Shape.width = width
        Shape.height = height
      

shape1 = Shape(5, 3)
print(shape1.width, shape1.height)