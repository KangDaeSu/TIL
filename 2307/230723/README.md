# 인스턴스와 메서드
  - "hello".upper()
    문자열.대문자로()
    객체.행동()
    인스턴스.메서드()

  - [1, 2, 3].sort()
    리스트.정렬해()
    객체.행동()
    인스턴스.메서드()

  - 하나의 객체는 특정 타입의 인스턴스이다.

  - 객체의 특징
    - 타입(type) : 어떤 연산자와 조작(method)이 가능한가?
    - 속성 : 어떤 상태(데이터)를 가지는가?
    - 조작법 : 어떤 행위(함수)를 할 수 있는가?
-------
# 클래스
- 클래스 : 파이썬에서 타입을 표현하는 방법
  - 객체를 생성하기 위한 설계도<br>
    데이터와 기능을 함께 묶는 방법을 제공
  - 생성자 함수
    - 객체를 생성할 때 자동으로 호출되는 특별한 메서드
    - __init__이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당
    - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
- 인스턴스 변수
  - 인스턴스(객체)마다 별도로 유지되는 변수
  - 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화됨
- 클래스 변수
  - 클래스 내부에 선언된 변수
  - 클래스로 생성된 모든 인스턴스들이 공유하는 변수
- 인스턴스 메서드
  - 각각의 인스턴스에서 호출할 수 있는 메서드
  - 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행

- 인스턴스와 클래스 간의 이름 공간(namespace)
  - 클래스를 정의하면, 클래스와 해당하는 