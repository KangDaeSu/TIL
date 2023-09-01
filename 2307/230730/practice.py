'''
a_nested_list = [0, [1, [2, [3, 4], 5]], 6, [7, 8, 9], 10]

# 1-1)
print(a_nested_list[3][0])

# 1_2)
print(a_nested_list[1][1])

# 1_3)
print(a_nested_list[1][1][1][1])

# 2
print("1. 참가 여부 확인 \n2. 참가 신청 \n3. 참가 취소 \n4. 참가자명 변경\n5. 참가명단 확인 \n6. 참가 인원수 확인 \n9. 종료")
nums = input()

def program(nums, person):
    try:
        num_1 = int(nums)
        if num_1 == 1:
            print("확인할 이름을 입력하세요: ")
            name_1 = input()
            if name_1 not in person:
                return "등록된 이름이 없습니다."
            else:
                return f'{name_1}는 등록된 사용자 입니다.'
        elif num_1 == 2:
            name_2 = input("참가자 이름을 입력해주세요: ")
            person.append(name_2)
            return person
        elif num_1 == 3:
            name_3 = input("취소할 이름을 입력하세요: ")
            person.remove(name_3)
            return person
        elif num_1 == 4:
            name_4 = input("등록할 이름을 입력하세요.")
            person.append(name_4)
            name_5 = input("수정할 이름을 입력하세요")
            person.remove(name_5)
            return person
        elif num_1 == 5:
            return person
        elif num_1 == 6:
            return len(person)
        elif num_1 == 9:
            exit
    except ValueError:
        return "정수를 입력하세요."

person = []
result = program(nums, person)
print(result)


# 추가문제 1_1)
result = [3 * i for i in range(1,6)]
print(result)

# 추가 문제 1_2)
import math
result = [math.exp(i * 3) for i in range(1,6)]
print(result)

# 추가 문제 1_3)
response = [i for i in range(1,21) if i % 2 != 0 if i % 3 != 0]
print(response)

# 추가 문제 1_4)
result = [(i, i**2) for i in range(1, 10, 2) ] 
print(result)

# 추가 문제 2_1)
animal_1 = ['dog', 'cat']
animal_1[0:2] = 'dog', 'cat', ['tiger','eagle']
print(animal_1)

# 추가 문제 2_2)
animal_1 = ['dog', 'cat']
animal_2 = ['tiger', 'eagle']
animal_1.append(animal_2)
print(animal_1)

# 추가 문제 2_3)
animal_1 = ['dog', 'cat']
animal_1.extend([['tiger','eagle']])
print(animal_1)


# 추가 문제 2_4
animal_1 = ['dog', 'cat']
animal_1.insert(2,['tiger','ealge'])
print(animal_1)
'''
# 추가 문제 3
def abc(chr):
    list_str = list(chr)
    list_str.sort()
    text = ''.join(list_str)
    print(text)

print(abc('dog'))
# 추가 문제 4_1)
# 추가 문제 4_2)
# 추가 문제 4_3)
