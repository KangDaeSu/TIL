import sys
sys.stdin = open("1974.txt","r")

T = int(input())
ans = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    

    result = 1
    while result == 1:
        for r in range(9):
            new_lst1 = [0]*9
            new_lst = [0]*9
            for c in range(9):
                new_lst1[c] = arr[r][c]  # 가로
                new_lst[c] = arr[c][r]   # 세로
        
            for k in ans:
                if k not in new_lst1 or k not in new_lst:
                    result = '0'
                    break
        di = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        dj = [-1, -1, -1, 0, 0, 0, 1, 1, 1]  
        for i in range(1, 9, 3): # 3 x 3 네모
            for j in range(1, 9, 3):
                new_lst2 = [0]*9
                for k in range(9):
                    new_lst2[k] = arr[i+di[k]][j+dj[k]]
                
                for l in ans:
                    if l not in new_lst2:
                        result = '0'
                        break
        break
    print(f'#{tc} {result}')
    


    
    




