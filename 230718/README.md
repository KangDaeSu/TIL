## Data Types
# **Data Types**
- 개요 : 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성
- **데이터 타입 분류**
  - Numeric Types
    - int(정수), float(실수), complex(복소수)
  - Text Sequence Types
    - str(문자열)
  - Sequence Types
    - list, tuple, range
  - Non-sequence Types
    - set, dict
  - 기타
    - Boolean, None, Functions

- **데이터 타입이 필요한 이유**
  - 값들을 구분하고, 어떻게 다뤄야 하는지를 알 수 있음
  - 요리 재료마다 특정한 도구가 필요하듯이 각 데이터 타입 값들도 각자에게 적합한 도구를 가짐
  - 타입을 명시적으로 지정하면 코드를 읽는 사람이 변수의 의도를 더 쉽게 이해할 수 있고, 잘못된 데이터 타입으로 인한 오류를 미리 예방
---
# **Numeric Types**
- **int 정수 자료형** : 정수(음수, 0, 양수)를 표현하는 자료형
- **진수 표현**
  - 2진수(binary) : 0b
    - print(0b10) => 2
  - 8진수(otal) : 0o
    - print(0o30) => 24
  - 16진수(hexadecimal) : 0x
    - print(0x10) => 16
- **float 실수 자료형** : 프로그래밍 언어에서 float는 실수에 대한 근삿값

- **유한 정밀도**
  - 컴퓨터 메모리 용량이 한정돼 있고 한 숫자에 대해 저장하는 용량이 제한 됨
  - 0.66666666666666과 1.6777777777777은 제한된 양의 메모리에 저장할 수 있는 2/3과 5/3에 가장 가까운 값
  - 0.666666666666666
  <br> print(2/3)
  - 1.67777777777777777
  <br> print(5/3)
<br>
<br>
- **실수 연산 시 주의사항**
  - 컴퓨터는 2진수를 사용, 사람은 10진법을 사용
  - 이때 10진수 0.1은 2진수로 표현하면 0.0001100110011001100110...-같이 무한대로 반복
  - 무한대 숫자를 그대로 저장할 수 없어서 사람이 사용하는 10진법의 근사값만 표시
  - 0.1의 경우 36028701896397 / 2**55이며 0.1에 가깝지만 정확히 동일하지는 않음
  - 이런 과정에서 예상치 못한 결과가 나타남
  - 이런 증상을 *Floating point rounding error*라고 함
<br>
<br>
- **실수 연산 시 해결책**
  - 두 수의 차이가 매우 작은 수보다 작은지를 확인하거나 math 모듈 사용
  <br> a = 3.2 - 3.1 => 0.1000000000000000009
  <br> b = 1.2 - 1.1 => 0.0999999999999999987
    1. 임의의 작은 수 활용
    <br>print(abs(a-b) <= 1e-10) => True
    2. math 모듈 활용
    <br>import math
    <br>print(math.isclose(a, b)) => True
<br>
<br>
- **지수 표현 방식**
  - e 또는 E를 사용한 지수 표현
    - 314 * 0.01
    <br> number = 314e-2
    - float
    <br> print(type(number))
    - 3.14
    <br> print(number)
----------
# **Sequence Types**
- **Sequence Types** : 여러 개의 값들을 **순서대로 나열하여 저장하는** 자료형 (str, list, tuple, range)

- **Sequence Type 특징** 
  1. 순서
    - 값들이 순서대로 저장(정렬x)
  2. 인덱싱
    - 각 값에 고유한 인덱스(번호)를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정할 수 있음
  3. 슬라이싱
    - 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
  4. 길이
    - len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
  5. 반복
    - 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음
------
# **str 문자열**
- **str** : 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형
- 문자열 표현
  - 문자열은 단일 문자나 여러 문자의 조합으로 이루어짐
  - 작은따옴표(') 또는 큰따옴표(") 감싸서 표현
  - Hello, World!
  <br>print('Hello, World!')
  - str
  <br>print(type('Hello, World!'))

- **중첩 따옴표**
  - 따옴표 안에 따옴표를 표현할 경우
    - 작은 따옴표가 들어 있는 경우는 큰 따옴표로 문자열 생성
    <br> 문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.
    <br>print("문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.")
    - 큰따옴표가 들어 있는 경우는 작은 따옴표로 문자열 생성
    <br> 문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.
    <br>print('문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.')

- **Escape sequence**
  - 역슬래시(backslash)뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
  - 파이썬의 일반적인 문법 규칙을 잠시 탈출한다는 의미
  <br>
  <br>
Escape sequence
    |예약 문자|내용(의미)|
    |:---:|:---:|
    |\n|줄 바꿈|
    |\t|탭|
    | \\ |백슬래시|
    |\’|작은 따옴표|
    |\"|큰   따옴표|

- **String Interpolation** : 문자열 내에 변수나 표현식을 삽입하는 방법
- **f-string** : 문자열에 f 또는 F 접두어를 붙이고 표현식을 {expression}로 작성하여 문자열에 파이썬 표현식의 값을 삽입할 수 있음
- **인덱스(index)** : 시퀀스 내의 값들에 대한 고유한 번호로, 각 값의 위치를 식별하는 데 사용되는 숫자
  - index 예시
    |"|h|e|l|l|o|"|
    |---:|:---:|:---:|:---:|:---:|:---:|---|
    |index|0|1|2|3|4||
    |index|-5|-4|-3|-2|-1||
- **슬라이싱(slicing)** : 시퀀스의 일부분을 선택하여 추출하는 작업 => 시작 인덱스와 끝 인덱스를 지정하여 해당 범위의 값을 포함하는 새로운 시퀀스를 생성 (슬라이싱을 할때 글자가 아닌 글자 사이의 공간을 슬라이싱 한다고 생각하면 쉬움)
  - step을 지정하여 추출
```python
my_str = 'hello'
my_str[0:5:2]
```
|"|<span style='color:red;'>h</span>|e|<span style='color:red;'>l</span>|l|<span style='color:red;'>o</span>|"|
|---:|:---:|:---:|:---:|:---:|:---:|---|
|index|<span style='color:yellow;'>0</span>|1|<span style='color:yellow;'>2</span>|3|<span style='color:yellow;'>4</span>||
|index|-5|-4|-3|-2|-1||

  - step이 음수일 경우
```python
my_str = 'hello'
my_str[::-1]
```

|"|<span style='color:red;'>h</span>|<span style='color:red;'>e</span>|<span style='color:red;'>l</span>|<span style='color:red;'>l</span>|<span style='color:red;'>o</span>|"|
|---:|:---:|:---:|:---:|:---:|:---:|---|
|index|0|1|2|3|4||
|index|<span style='color:yellow;'>-5</span>|<span style='color:yellow;'>-4</span>|<span style='color:yellow;'>-3</span>|<span style='color:yellow;'>-2</span>|<span style='color:yellow;'>-1</span>||

  - 문자열은 불변 (변경 불가)
```python
my_str = 'hello'

# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'
```
 - 새로운 문자열을 만들 생각으로 문제에 접근
------
# **list 리스트**
- **ist** : 여러 개의 값을 순서대로 저장하는 **변경 가능한** 시퀀스 자료형

- **리스트 표현**
  - 0개 이상의 객체를 포함하며 데이터 목록을 저장
  - 대괄호([])로 표기
  - 데이터는 **어떤 자료형도 저장**할 수 있음
    ```python
    my_list_1 = []

    my_list_2 = [1, 'a', 3, 'b', 5]

    my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
    ```
- **리스트의 시퀀스 특징**
  ```python
    my_list = [1, 'a', 3, 'b', 5]

    # 인덱싱
    print(my_list[1])  # a

    # 슬라이싱
    print(my_list[2:4])  # [3, 'b']
    print(my_list[:3])  # [1, 'a', 3]
    print(my_list[3:])  # ['b', 5]
    print(my_list[0:5:2])  # [1, 3, 5]
    print(my_list[::-1])  # [5, 'b', 3, 'a', 1]

    # 길이
    print(len(my_list))  # 5
    ```
- **중첩된 리스트 접근**
  - 출력 값 예상해보기
  ```python
    my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]

    print(len(my_list))  
    print(my_list[4][-1])  
    print(my_list[-1][1][0]) 
- **리스트는 가변 (변경가능)**
  ```python
    my_list = [1, 2, 3]
    my_list[0] = 100

    print(my_list)  # [100, 2, 3]
    ```
---
# **tuple 튜플**
- **튜플** : 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형

- **튜플 표현**
  - 0개 이상의 객체를 포함하며 데이터 목록을 저장
  - 소괄호(())로 표기
  - 데이터는 어떤 자료형도 저장할 수 있음
     ```python
    my_tuple_1 = ()

    my_tuple_2 = (1,)

    my_tuple_3 = (1, 'a', 3, 'b', 5)
    ```
- **튜플의 시퀀스 특징**
    ```python
    my_tuple = (1, 'a', 3, 'b', 5)

    # 인덱싱
    print(my_tuple[1])  # a

    # 슬라이싱
    print(my_tuple[2:4])  # (3, 'b')
    print(my_tuple[:3])  # (1, 'a', 3)
    print(my_tuple[3:])  # ('b', 5)
    print(my_tuple[0:5:2])  # (1, 3, 5)
    print(my_tuple[::-1])  # (5, 'b', 3, 'a', 1)

    # 길이
    print(len(my_tuple))  # 5
    ```

- **튜플은 불변 (변경 불가)**
  ```python
    my_tuple = (1, 'a', 3, 'b', 5)

    # TypeError: 'tuple' object does not support item assignment
    my_tuple[1] = 'z'
    ```

- **튜플은 어디에 쓰일까?**
  - 튜플은 불변 특성을 사용한 안전하게 여러 개의 값을 전달, 그룹화, 다중 할당 등 개발자가 직접 사용하기 보다 '파이썬 내부 동작'에서 주로 사용됨
     ```python
        x, y = (10, 20)

        print(x)  # 10
        print(y)  # 20

        # 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
        x, y = 10, 20
        ```
----
# **range**
- **range** : 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형

- **range 표현 1**
  - range(n)
    - 0부터 n-1까지의 숫자의 시퀀스
  - range(n, m)
    - n부터 m-1까지의 숫자 시퀀스

- **range 표현 2**
  - 주로 반복문과 함께 사용 예정
---
# **Non-sequence Types**
- **dict 딕셔너리** : key-value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

- **딕셔너리 표현**
  - key는 변경 불가능한 자료형만 사용 가능(str, int, float, tuple, range ...)
  - value는 모든 자료형 사용 가능
  - 중괄호({})로 표기
       ```python
        my_dict_1 = {}
        my_dict_2 = {'key': 'value'}
        my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

        print(my_dict_1)  # {}
        print(my_dict_2)  # {'key': 'value'}
        print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}
        ```

- **딕셔너리 사용**
  - key를 통해 value에 접근
        ```python
        my_dict = {'apple': 12, 'list': [1, 2, 3]}

        print(my_dict['apple'])  # 12
        print(my_dict['list'])  # [1, 2, 3]

        # 값 변경
        my_dict['apple'] = 100
        print(my_dict)  # {'apple': 100, 'list': [1, 2, 3]}
        ```
---
# **set**
- **set 세트** : 순서와 중복이 없는 변경 가능한 자료형

- **세트 표현**
  - 수학에서의 집합과 동일한 연산 처리 가능
  - 중괄호({})로 표기
       ```python
        my_set_1 = set()
        my_set_2 = {1, 2, 3}
        my_set_3 = {1, 1, 1}

        print(my_set_1)  # set()
        print(my_set_2)  # {1, 2, 3}
        print(my_set_3)  # {1}
    ```

- **세트의 집합 연산**
  ```python
    my_set_1 = {1, 2, 3}
    my_set_2 = {3, 6, 9}

    # 합집합
    print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}

    # 차집합
    print(my_set_1 - my_set_2)  # {1, 2}

    # 교집합
    print(my_set_1 & my_set_2)  # {3}
    ```
---
# **Other Types**

- **None** : 파이썬에서 '값이 없음'을 표현하는 자료형

- **None 표현**
  ```python
    variable = None

    print(variable)  # None
    ```

- **Boolean** : 참(Ture)과 거짓(False)을 표현하는 자료형
  - 비교 / 논리 연산의 평가 결과로 사용됨
  - 주로 조건 / 반복문과 함께 사용
        ```python
        bool_1 = True
        bool_2 = False

        print(bool_1)  # True
        print(bool_2)  # False
        print(3 > 1)  # True
        print('3' != 3)  # True
        ```

- **Collection** : 여러 개의 항목 또는 요소를 담는 자료 구조 str, list, tuple, set, dict

- 컬렉션 정리
    |컬렉션|변경 가능 여부|나열, 순서||
    |:---:|:---:|:---:|:---:|
    |str|X|O|시퀀스|
    |list|O|O|시퀀스|
    |tuple|X|O|시퀀스|
    |set|O|X|비시퀀스|
    |dict|O|X|비시퀀스|

- 불변과 가변의 차이(1/2)
    ```
    my_str = 'hello'
    # TypeError: 'str' object does not support item assignment
    my_str[0] = 'z'

    my_list = [1, 2, 3]
    my_list[0] = 100
    # [100, 2, 3]
    print(my_list)
    ```
----
## **얇은 복사, 깊은 복사**

  ```python
  # 리스트의 특징(문제점)
  l = [1, 2, 3]
  b_l = l
  l[2] = 1000
  print('l=', l, 'b_l=', b_l)

  # 얕은 복사
  l = [1, 2, 3]
  b_l = l[::smirk:
  l[2] = 1000
  print('l=', l, 'b_l=', b_l)

  # 2차원에서 얕은 복사의 문제점
  l = [[2, 3, 4], [3, 4, 5], [4, 5, 6]]
  b_l = l[::smirk:
  l[0][2] = 1000
  print('l=', l, 'b_l=', b_l)

  # 깊은 복사
  import copy
  l = [[2, 3, 4], [3, 4, 5], [4, 5, 6]]
  b_l = copy.deepcopy(l)
  l[0][2] = 10000
  print('l=', l, 'b_l=', b_l)
  ```

---
# **Type Conversion**
1. 암시적 형변환 : 파이썬이 자동으로 형변환을 하는 것
  - Boolean과 Numeric Type에서만 가능
  
2. 명시적 형변환
  - 개발자가 직접 형변환을 하는것
  - 암시적 형변환이 아닌 경우를 모두 포함
  - str -> integer : 형식에 맞는 숫자만 가능
  - integer -> str : 모두 가능

---
# 단축평가
- 단축평가 : 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작

- 단축평가 동작
  - and
    - 첫 번째 피연산자가 False인 경우, 전체 표현식은 False로 결정
    <br> 두 번째 피연산자는 평가되지 않고 그 값이 무시

    - 첫 번째 피연산자가 True인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정.
    <br> 두 번째 피연산자가 평가되고 그 결고가 전체 표현식의 결과로 반환

  - or
    - 첫 번째 피연산자가 True인 경우, 전체 표현식은 True로 결정.
    <br> 두 번째 피연산자는 평가되지 않고 그 값이 무시

    - 첫 번째 피연산자가 False인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정.
    <br> 두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환
  
  - 단축평가 이유 : 코드 실행을 최적화하고, 불필요한 연산을 피할 수 있도록 함
