# 비트 연산

## 비트 연산자

|연산자|연산자의 기능|예시|
|---|---|----|
|&|비트단위로 AND 연산을 한다|num1 & num2|
|'shift+ \ \'|비트단위로 OR 연산을 한다|num1 \ num2|
|^|비트단위로 XOR 연산을 한다.(같으면 0, 다르면 1)|num1 ^ num2|
|~|단항 연산자로서 피연산자의 모든 비트를 반전시킨다|~num|
|<<|피연산자의 비트 열을 왼쪽으로 이동시킨다.|num<<2|
|>>|피연산자의 비트 열을 오른쪽으로 이동시킨다.|num>>2|

 - 1 << 
   - 2**n 의 값을 갖는다.
   - 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
   - Power set(모든 부분 집합)
     - 공집합과 자기 자신을 포함한 모든 부분집합
     - 각 원소가 포함되거나 포함되지 않는 2가지 경우의 수를 계산하면 모든 부분집합의 수가 계산된다.

 - i & (1 << j)
   - 계산 결과는 i의 j번째 비트가 1인지 아닌지를 의미한다.

# 순열
  - 서로 다른 것들 중 몇개를 뽑아서 한 줄로 나열하는 것
  - 서로 다른 n개 중 r개를 택하는 순열은 아래와 같이 표현한다.
    - nPr
  - 그리고 nPr은 다음과 같은 식이 성립한다.
    - nPr = n x (n-1) x (n-2) x ... x(n-r+1)
  - nPn = n!이라고 표기하며 Factorial이라 부른다.
    - n! = n x (n-1) x (n-2) x ... x 2 x 1
  - 다수의 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련 있다.
  - N개의 요소들에 대해서 n!개의 순열들이 존재한다.
  - 단순하게 순열을 생성하는 방법
    - ex) {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수
      - 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop을 이용해 구현할 수 있다.
```py
# 재귀 순열

def perm(k):
  # if k == 3: 4P3
  if k == N:
    print(bits)
    for i in range(4):
      pos = bits[i]
      print(numbers[pos], end=' ')
    print()
    return
  
  for i in range(N):
    if not used[i]:
      bits[k] == i
      used[i] = True
      perm(k + 1)
      used[i] = False

N = 4
numbers = [8, 10, 20, 3]

bits = [-1] * N
used = [False] * N
perm(0)

```
  
# 부분 집합
  - 집합에 포함된 원소들을 선택하는 것이다.
  - 다수의 중요 알고리즘들이 원소들의 그룹에서 최적의 부분 집합을 찾는 것이다.
  - N 개의 원소를 포함한 집합
    - 자기 자신과 공집합을 포함한 모든 부분집합(power set)의 개수는 2**n개
    - 원소의 수가 증가하면 부분집합의 개수는 지수적으로 증가
  - 바이너리 카운팅을 통한 사전적 순서(Lexicographic Order)
    - 부분집합을 생성하기 위한 가장 자연스러운 방법이다.
    - 바이너리 카운팅(Binary Counting)은 사전적 순서로 생성하기 위한 가장 간단한 방법이다.
    - 바이너리 카운팅(Binary Counting)
      - 원소 수에 해당하는 N개의 비트열을 이용한다.
      - n번째 비트값이 1이면 n번째 원소가 포함되었음을 의미한다.

```py
# 재귀 부분집합

def partial(k, sumV, zlist, olist):
  # if ... => 백트래킹 조건
  if k == N:
    # print(bits)
    # print(sumV, zlist, olist)
    return
    
  bits[k] = 0
  partial(k + 1, sumV + 0, zlist[numbers[k]], olist + [numbers[k]])
  bits[k] = 1
  partial(K + 1, sumV + numbers[k], zlist, olist + [numbers[k]])

N = 4
numbers = [8, 10, 20, 3]
bits = [-1] * N
sumV = 0
zlist = []
olist = []
partial(0, sumV, zlist, olist)

```

# 조합
  - 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합(combination)이라고 부른다.
  - 조합의 수식
    - nCr = n! / (n-r)!r!, (n >= r) <br>
      nCr = (n-1)C(r-1) + (n-1)Cr => 재귀적 표현 <br>
      nC0 = 1

```python
# 재귀 조합

def nCr(n, r):
  if r == 0:
    print(tr)

  elif n < r: # 남은 원소보다 많은 원소를 선택해야 하는이유
    return  # 불가

  else:
    tr[r-1] = a[n-1]  
    nCr(n-1, r-1)
    nCr(n-1, r)

N = 5
R = 3
a = [1, 2, 3, 4, 5]
tr = [0] * R
nCr(N, R)

```