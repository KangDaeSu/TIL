## Control of flow
# 제어문
- 제어문(contol statement) : 코드의 실행 흐름을 제어하는데 사용되는 구문
<br>                조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행
----
# 조건문
- 조건문(conditional statement) : 주어진 조건식을 평가하여 해당 조건이 참(Treu)인 경우에만 코드 블록을 실행하거나 건너뜀

- if
 ```python
if 표현식:
   코드 블록
elif 표현식:
    코드블록
```

- ex)
```python
num = int(input('숫자를 입력하세요 : ')) # 정수로 입력을 받음

#if statement
#numd이 홀수라면(2로 나눈 나머지가 1이라면)
if num %2 == 1: #=> if num % 2: 결과값이 1이라면 True 판정
    print("홀수입니다.")
#num이 홀수가 아니라면(짝수면)
else:
    print("짝수입니다.")
```
---
# 반복문
# for
- for : 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
```python
for 변수 in 반복 가능한 객체:
    코드 블록
```
- 요소 순서대로 반복하여 돌아감
- 반복 가능한 객체(iterable) : 반복문에서 순회할 수 있는 객체
<br> 시퀀스 객체 뿐만 아니라 dict, set 등도 포함

- 인덱스로 리스트 순회
  - 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
   ```python
    numbers = [4, 6, 10, -8, 5]
    
    for i in range(len(numbers)): # 재사용을 위해 len을 사용
        numbers[i] = numbers[i] * 2
    
    print(numbers) # [8, 12, 20, -16, 10]
    ``` 

- 중첩된 반목문
  - 안쪽 반복문은 outers 리스트의 각 항목에 대해 한 번씩 실행됨
  - print가 호출되는 횟수 => len(outers) * len(inners)
 ```python
    outers = ['A', 'B']
    inners = ['c', 'd']
    
    for outer in outers:
        for inner in inners:
            print(outer, inner)
    
    """
    A,c
    A,d
    B,c
    B,d
    """
```
- 중첩 리스트 순회
  - 안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회
---------
# while
- while : 주어진 조건식이 참인 동안 코드를 반복해서 실행 
<br>== 조건식이 거짓가 될 때 까지 반복

- while의 구조
```python
    while 조건식:
        코드 블록
```

- ex)
```python
a = 0

while a < 3:
    print(a)
    a += 1

print('끝')

"""
0
1 
2 
끝
"""
```

- 사용자 입력에 따른 반복
  - while 문을 사용한 특정 입력 값에 대한 종료 조건 활용하기
   
    ```python
    number = int(input('양의 정수를 입력해주세요.: '))

    while number <= 0:
        if number < 0:
            print('음수를 입력했습니다.')
        else:
            print('0은 양의 정수가 아닙니다.')

        number = int(input('양의 정수를 입력해주세요.: '))

    print('잘했습니다!')
    """
    양의 정수를 입력해주세요.: 0
    0은 양의 정수가 아닙니다.  
    양의 정수를 입력해주세요.: -1
    음수를 입력했습니다.       
    양의 정수를 입력해주세요.: 1
    잘했습니다!
    """
    ```
- while문은 반드시 **종료조건** 필요

- 적절한 반복문 활용하기
 - for
   - 반복 횟수가 명확하게 정해져 있는 경우에 유용
   - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때

  - while
    - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
    - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만<br>
때때로 일부만 실행하는 것이 필요할 때가 있음
- break : 반복을 즉시 중지

- continue : 다음 반복으로 건너뜀

- break와 continue 주의사항
- break와 continue를 남용하는 것은 코드의 가독성을 저하시킬 수 있음
- <span style='color:red;'>특정한 종료 조건</span>을 만들어 break을 대신하거나,<br> <span style='color:red;'>if 문을 사용</span>해 continue 처럼 코드를 건너 뛸 수도 있음
- 약간의 시간이 들더라도 가능한 코드의 가독성을 유지하고 코드의 의도를<br> 명확하게 작성하도록 노력하는 것이 중요

- 수정 전
    ```python
    for number in range(1, 5):
        if number == 3:
            continue
        print(number)
    """
    1
    2
    4
    """
    ```

- 수정 후
    ```python
    for number in range(1, 5):
        if number != 3:
            print(number)
    """
    1
    2
    4
    """
    ```
---
### List Comprehension

- List Comprehension : **간결**하고 **효율적인 리스트 생성** 방법

- List Comprhension 구조
[expression for 변수 in iterable]
<br> list(expression for 변수 in iterable)

- ex)
```python
# 0~9 요소를 가지는 리스트 만들기
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i) # 리스트안에 i를 넣는 함수
print(new_list)

# [1, 3, 5, 7, 9]

# 2. list comprehension
new_list_2 = [i for i in range(10) if i % 2 == 1] # i 안에 range의 결과를 넣어 리스트로 만듬
# 엔터 없이 코드를 한줄로 이어 적음.
print(new_list_2)

#[1, 3, 5, 7, 9]
```

- 단계적인 코드 블록 보다 가독성이 떨어지지만 사용법은 아는게 좋음. (남용하지 말자)

-------
# 참고
- pass : 아무런 동작도 수행하지 않고 넘어가는 역할
<br> 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지 않아야 할 때 사용

- 예시
  1. 코드 작성 중 미완성 부분
    - 구현해야 할 부분이 나중에 추가될 수 있고,
코드를 컴파일하는 동안 오류가 발생하지 않음
 ```python
        def my_function():
            pass  
```

  2. 조건문에서 아무런 동작을 수행하지 않아야 할 때

    ```python
    if condition:
        pass # 아무런 동작도 수행하지 않음
    else:
        # 다른 동작 수행
    ```
  
  3.무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 <br>루프를 계속 진행하는 방법

    ```python
    while True:
        if condition:
            break
        elif condition:
            pass  # 루프 계속 진행
        else:
            print('..')
    ```

- enumerate : iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

- 예시
```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
print(f'인덱스 {index}: {fruit}')

"""
인덱스 0: apple
인덱스 1: banana
인덱스 2: cherry
"""
```
---
# 이외
```python
# 0~9 요소를 가지는 리스트 만들기
# 1. 일반적인 방법
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i) # 리스트안에 i를 넣는 함수
    else:
        new_list.append(str(i))
print(new_list)

# 2. list comprehension
new_list_2 = [i for i in range(10) if i % 2 == 1] # i 안에 range의 결과를 넣어 리스트로 만듬
# 엔터 없이 코드를 한줄로 이어 적음.
print(new_list_2)

new_list_3 = [i if i % 2 ==1 else str(i) for i in range(10)]
print(new_list_3)


['0', 1, '2', 3, '4', 5, '6', 7, '8', 9]
짝수는 문자열로 홀수는 숫자로 출력


# 리스트를 생성하는 3가지 방법 비교

numbers = ['1', '2', '3']
# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)
# [1, 2, 3]


# 2. map
new_numbers_2 = list(map(int, numbers)) # int함수를 numbers에 적용
print(new_numbers_2) 
# [1, 2, 3]

# 3. list comprehension
new_numbers_3 = [int(number) for number in numbers]
print(new_numbers_3)
# [1, 2, 3]

# enumerate
result = ['a','b', 'c']

print(enumerate(result))
#<enumerate object at 0x0000012B0F8F3900>

print(list(enumerate(result)))
# [(0, 'a'), (1, 'b'), (2, 'c')]
# 숫자는 해당 리스트열의 인덱스

for index, elem, in enumerate(result):
    print(index, elem)

# 어떤게 제일 빨라요?
# 성능 => 일반화가 불가능(외부요인, 상황)
# loop & map & comprehension

# - 대부분의 상황에서는 compre가 빠르다
# - 하지만 다른 함수, 내장함수에 따라 map이 더 빠른경우도 많았다.
# - 파이썬이 3.대 후반에 for loop 성능에 비약적인 향상이 있었음
# - 그래서 극단적인 차이는 존재하지 않는다.
# - 코드의 가독성 > 간결함
# 프로그래밍은 우리 프로그램이 어떻게 그 목적을 명확하게 전달하는지에 대한 것
# "작은 효율성에 대해서는, 말하자면 97% 정도에 대해서는 잊어버려라
# 섣부른 최적화는 모든 악의 근원이다." - 도널드 커누스
```
