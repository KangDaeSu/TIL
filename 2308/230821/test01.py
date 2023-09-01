#preorder
def pre_order(root):
    if root:
        print(root)
        pre_order(TREE[root][0])  # 왼쪽)
        pre_order(TREE[root][1])  # 오른쪽)

#postorder
def post_order(root):
    if len(G[root]) >= 1:
        post_order(G[root][0])
    if len(G[root]) == 2:
        post_order(G[root][1])
    print(root)

# inorder
def print_tree(root):
    if cl[root]:    # tree이면:
        print_tree(cl[root])    # root의 왼쪽 서브트리의 root)

    print(root)

    if cr[root]:    # 오른쪽이 tree이면:
        print_tree(cr[root])    # root의 오른쪽 서브트리의 root)

def print_tree2(root):
    if root:
        print_tree(cl[root])    # 왼쪽
        print(root)
        print_tree(cr[root])    # 오른쪽



# 트리
N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))

cl = [0] * (N+1)
cr = [0] * (N+1)
pn = [0] * (N+1)
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    pn[c] = p
    if cl[p] == 0:
        cl[p] = c
    else:
        cr[p] = c
print(pn)
print(cl)
print(cr)

TREE = [[0, 0, 0] for _ in range(N+1)]
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    if TREE[p][0] == 0:     # 왼쪽이 비어 있으면:
        TREE[p][0] = c
    else:
        TREE[p][1] = c

    TREE[c][2] = p
print(TREE)

G = [[] for _ in range(N+1)]
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    G[p].append(c)
print(G)