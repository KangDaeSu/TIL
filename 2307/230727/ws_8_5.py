# ws_8_5.py

class Dog:
    sound = '멍멍'

    def __init__(self):
        pass
    

class Cat:
    sound = '야옹'

    def __init__(self):
        pass
    

class Pet(Cat, Dog):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'
    

P1 = Pet()
print(P1)
