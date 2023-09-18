# 알고리즘 설계 기법의 종류

1. 전체를 다 보자(Brute Forece - 완전 탐색)
 - 배열 : 반복문을 다 돌리기
 - 그래프 : DFS, BFS
2. 상황마다 좋은 걸 고르자 (Greedy - 탐욕)
 - 규칙을 찾는 것
 - 주의사항 : 항상 좋은 것을 뽑아도, 최종 결과가 제일 좋다가 보장되지 않음
3. 하나의 큰 문제를 작은 문제로 나누어 부분적으로 해결하자
  (Dynamic Programming)
   - Memoization 기법을 활용
   - 점화식(bottom-up), 재귀(top-down)
4. 큰 문제를 작은 문제로 쪼개서 해결하자
  (Divide and Conquer - 분할 정복)
5. 전체 중, 가능성 없는 것을 빼고 보자
  (Backtracking - 백트래킹)
   - 가지치기

<hr>
<br>

# 분할 정복 기법
 ## 설계 전략
  - 분할(Divide) : 해결할 문제를 여럭 개의 작은 부분으로 나눈다. 
  - 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.
  - 통합(Combine) : (필요하다면) 해결된 해답을 모은다.

 ## 병합 정렬
  - 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

  - 분할 정복 알고리즘 활용
    - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄.
    - top-down 방식

  - 시간 복잡도
      O(n log g)  

  - 과정
    - 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.
      ```
      merge_sort(LIST m)
        IF length(m) == 1: RETURN m

        LIST left, right
        middle <- length(m) / 2
        FOR x in m befor middle
          add x to left
        For x in m atfer or equal middle
          add x to right

        left <- merge_sort(left)
        right <- merge_sort(right)

        RETURN merge(left, right)
      ```
    - 병합 단계 : 2개의 부분집합을 정렬하며넛 하나의 집합으로 병합
      ```
      merge(LIST left, LIST right)
        LIST result

        WHILE length(left) > 0 OR length(right) > 0
          IF length(left) > 0 AND length(right) > 0
            IF firtst(left) <= first(right)
              append popfirst(left) to result
            ELSE
              appen popfirst(right) to result
          ELIF length(left) > 0
            append popfirst(left) to reuslt
          ELIF lenth(right) > 0
            append popfirst(right) to result
        RETURN result
      ```
  - 구조가 변하지 않는다 => 재귀

<hr>
<br>

 ## 퀵 정렬
  - 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
    - 병합 정렬과 동일?
    
  - 다른점 1 : 병합 정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.

  - 다른점 2 : 각 부분 정렬이 끝난 후, 병합정렬은 "병합"이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다.

<hr>
<br>

 ## 이진 검색
  - 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
   - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

  - 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

  - 검색 과정
   1. 자료의 중앙에 있는 원소를 고른다.
   2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
   3. 목표 값이 중앙 원소의 값보다 작으면 자료의 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대하여 새로 검색을 수행한다.
   4. 찾고자 하는 값을 찾을 때 까지 1 ~ 3의 과정을 반복한다.
  

<hr>
<br>

  ## 분할 정복의 활용
   - 병합 정렬
    - 외부 정렬의 기본이 되는 정렬 알고리즘이다. 또한, 멀티코어(Multi-Core) CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용된다.

   - 퀵 정렬
    - 평균적으로 굉장히 좋음 O(NlogN)
    -  매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘이다.
    -  단점 : 역순 정렬 등 최악의 경우 O(N^2) => 특수한 케이스

   - 이진 검색
    - 코딩 테스트의 메인 알고리즘 중 하나
    - 목적 : "원하는 값을 빨리 찾는 것"
    - 시간 : O(logN)
    - Parametirc Search => 특정 범위 검색
     - lower bound
     - upper bound
     - 여러 개의 데이터 중 2가 처음 나온 시점
     - 2~9 사이의 데이터는 몇 개인가?