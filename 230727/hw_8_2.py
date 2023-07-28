def check_number():
    while True:
        try:
            num = int(input('숫자를 입력하세요: '))
            if num > 0:
                print('양수입니다.')
            elif num == 0:
                print('0입니다.')
            elif num < 0:
                print('음수입니다.')
        except ValueError:
            print('잘못된 입력입니다.')
            break
        except:
            print('다시 입력해주세요.')
            break

check_number()