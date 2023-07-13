# TIL
## 2023-07-12 ~ 2023-07-13
Markdown : 일반 텍스트로 문서를 작성하는 간단한 방법.<br>"# ~~" : 문서의 단계별 제목으로 사용, '#'의 개수에 따라 제목의 수준 구별. 
<br> 리스트 : '번호' -> 순서를 표시하는 리스트, '-' -> 순서가 없는 리스트 
,' \``` 공백 ``` ' : 네모상자
```
 [](링크주소): 링크 삽입
![](링크주소) : 이미지 삽입 * 이미지의 너비와 높이는 마크다운으로 조절 불가.
** ** : 굵게
* * : 기울임
~~ ~~ : 취소선
--- : 단락 구분 수평선
 ```
[Markdown Guide](https://www.markdownguide.org/basic-syntax/)
<br>[MarkText](https://github.com/marktext/marktext#download-and-installation)
---

<br> CLI(Command Line Interface) : 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식
<br> 기초문법
<br> . : 현재 디렉토리, .. : 현재의 상위 디렉토리
<br> touch : 파일 생성
<br> mkdir : 새 디렉토리 생성
<br> ls : 현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 출력
<br> cd : 현재 작업 중인 디렉토리를 변경(위치이동)
<br> start : 폴더/파일 열기
<br> rm : 파일 삭제 (-r 옵션을 사용해 디렉토리 삭제)
---
## git
<br> **분산 버전 관리 시스템**
<br> ●장점 
<br> - 중앙 서버에 의존하지 않고도 동시에 다양한 작업을 수행할 수 있음 -> 개발자들 간의 작업 충돌을 줄여주고 개발 생산성을 향상
<br> - 중앙 서버의 장애나 손실에 대비하여 백업과 복구가 용이
<br> - 인터넷에 연결되지 않은 환경에서도 작업을 계속할 수 있음 -> 변경 이력과 코드를 로컬 저장소에 기록하고, 나중에 중앙 서버와 동기화
<br>
<br> ● git의 3가지 영역
<br> - Working Directory : 실제 작업 중인 파일들이 위치하는 영역
<br> - Staging Area : Wokring Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
<br> - Repository : 버전 이력과 파일들이 영구적으로 저장되는 영역으로 모든 버전과 변경 이력이 기록됨
<br> - Commit : 변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다 하여 'snapshot'이라고도 함
<br>
<br> ● 간단한 코드
<br> git init : git의 버전 관리를 시작할 디렉토리에서 진행 ※ 같은 파일안에 .git의 파일이 2개 존재 하지 않도록 주의
<br>
<br> git add : 변경사항이 있는 파일을 staging area에 추가
<br> git commit -m " " : staging area에 있는 파일들을 저장소에 기록 -> 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
<br> ● 사용자 정보 등록 
<br> - git config --global user.email "메일주소"
<br> - git config --global user.name "유저네임"
<br> - git log : commit 목록 확인
<br> - git status : 로컬 저장소의 파일 상태 확인
---
<br>
<br>c 언어 : 메모리를 직접적으로 컨트롤 가능 => 효율적인 프로그램 구성 가능
단, 매우 어려움

python : c에 비하여 쉬움, 많은 사람들이 사용, 많은 것을 할 수 있음.
1. 대/소문자 구별
2. 띄어쓰기
3. 스펠링

저장 : 메모리에 쌓임(박스)
print(2+3) => 5

1000번지에 데이터 10을 저장해라

사용자로 입력을 받아서 +3을 해서 출력해줘
a = 입력을 받는다
print(a+3)

dust = 60 : dust라는 빈 공간을 설정하고 그 안에 60의 값을 넣는다.

숫자, 글자, 참/거짓 저장 가능

print(hello) : hello 변수에 담긴 내용을 출력해주세요.
print('hello') : 'hello'라는 글자를 출력해주세요.

조건
if True:
  print('조건문입니다.')

if/else
if dust>50:
	print('50초과')
else:
	print('50이하')
if dust > 150:
	print('매우나쁨)
elif 조건:
	print("나쁨")
else : 
	print("좋음")

while
while True: (무한하게 돌게된다)
    print('계속해주세요')