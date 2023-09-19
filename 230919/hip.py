# 최대 힙 - 삽입

def enque(item):
    global hsize

    hsize += 1
    TREE[hsize] = item

    c = hsize
    p = c // 2
    while p and TREE[p] < TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p
        p = c // 2


def deque():
    global hsize

    result = TREE[1]
    TREE[1] = TREE[hsize]
    hsize -= 1

    p = 1
    c = p * 2
    while c <= hsize:
        if c+1 <= hsize and TREE[c] < TREE[c+1]:
            c = c + 1
        if TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            p = c
            c = p * 2
        else:
            break
    
    return result

TREE = [0, 20, 15, 19, 4, 13, 11]
TREE += [0] * 100

hsize = 6
enque(23)
print(TREE)
enque(17)
print(TREE)

print(deque())
print(TREE)