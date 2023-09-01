# 마이쮸

total = 20
Q = []
newh = 1
sumV = 0
while sumV < total:
    print(Q)
    # - 처음 줄서는 사람
    Q.append((newh, 1))
    newh += 1
    #- 받아가는 사람
    h, candy = Q.pop(0)
    sumV += candy
    print(f'{h}가 {candy} 받아감')
    
    #- 받은 사람이 다시 줄서기
    Q.append((h, candy+1))
    
print(f'{h}가 마지막')

