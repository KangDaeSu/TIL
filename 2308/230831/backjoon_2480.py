n1, n2, n3 = map(int, input().split())

price = 0
if n1 == n2 and n2 == n3:
    price = 10000 + (n1 * 1000)
elif n1 == n2:
    price = 1000 + (n1 * 100)
elif n1 == n3:
    price = 1000 + (n1 * 100)
elif n2 == n3:
    price = 1000 + (n2 * 100)
else:
    price = 100 * max(price, n1, n2, n3)
print(price)