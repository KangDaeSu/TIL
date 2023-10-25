import sys
sys.stdin = open('input.txt', 'r')

def P(number):
    for k in range(3, int(number**(0.5))+1):
        if number % k == 0:
            return False

    return True

def dfs(num):
    if num >= 10 ** (N-1):
        print(num)
        return

    for j in [1, 3, 7, 9]:
        number = (num * 10) + j
        if P(number):
            dfs(number)

N = int(input())
for i in [2, 3, 5, 7]:
    dfs(i)