arr = [int(input()) for _ in range(9)]
arr.sort()

num = sum(arr)-100
for i in range(9):
    for j in range(i+1, 9):
        if arr[i] + arr[j] == num:
            num1 = arr[i]
            num2 = arr[j]
for k in arr:
    if k != num1 and k != num2:
        print(k)