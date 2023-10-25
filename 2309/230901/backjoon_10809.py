s = input()

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in lst:   # lst 의 요소가 s 안에 들어 있으면
    if i in s:
        print(s.index(i), end=' ')  # 인덱스의 첫 번째 위치를 출력
    else:
        print(-1, end=' ')  # 아니면 -1을 출력

