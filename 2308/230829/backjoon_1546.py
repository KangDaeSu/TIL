import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = list(map(int, input().split()))

sum_value = (((sum(lst) / max(lst)) * 100) / N)
print(sum_value)