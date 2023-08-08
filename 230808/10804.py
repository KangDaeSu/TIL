import sys
sys.stdin = open("10804.txt","r")

T = int(input())

for tc in range(1,T+1):
    my_str = input()
    
    result = my_str[::-1]
    new_str = ''
    for i in result:
        if i == 'p':
            new_str += 'q'
        elif i == 'q':
            new_str += 'p'
        elif i == 'b':
            new_str += 'd'
        elif i == 'd':
            new_str += 'b'


    print(f'#{tc} {new_str}')