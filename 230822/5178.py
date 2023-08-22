# 노드의 합
import sys
sys.stdin = open("5178.txt", "r")

def postorder(root):
    if root > N:
        return 0
    if TREE[root]:
        return TREE[root]

    vl = postorder(root * 2)
    vr = postorder(root * 2 + 1)
    TREE[root] = vl + vr
    return TREE[root]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    TREE = [0] * (N + 1)
    for _ in range(M):
        nodeNo, value = map(int, input().split())
        TREE[nodeNo] = value

    postorder(1)
    print(f'#{tc} {TREE[L]}')

    # for i in range(N, 0, -1):     # 완전 이진 트리에만 적용 가능
    #     TREE[i//2] += TREE[i]