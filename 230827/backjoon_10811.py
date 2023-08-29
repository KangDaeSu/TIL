N, M = map(int, input().split())
basket = [n for n in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    lst = basket[i-1:j]
    lst.reverse()
    basket[i-1:j] = lst

for i in range(N):
    print(basket[i], end=" ")