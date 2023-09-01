# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        while True:
            try:
                name = input("이름을 입력하세요: ")
                age = int(input("나이를 입력하세요: "))
                self.user_data = {'name': name, 'age': age}
                break
            except ValueError:
                print("나이는 숫자로 입력해야 합니다.")

    def display_user_info(self):
        try:
            name = self.user_data['name']
            age = self.user_data['age']
            print(f'사용자정보: \n이름을 입력하세요: {name} \n나이를 입력하세요: {age}')
        except KeyError:
            print("사용자 정보가 입력되지 않았습니다.")
        except:
            print("오류")

user = UserInfo()
user.get_user_info()
user.display_user_info()
