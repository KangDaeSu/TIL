# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self, num, str):
        for _ in range(num): # 단순 횟수 반복 for문 : for _ in range():
            print(str)
        
repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")