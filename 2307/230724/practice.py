# print(help(list))

# numbers = [1, 2, 3]

# # 1. 할당
# list1 = numbers

# # 2. 슬라이싱
# list2 = numbers[:]

# numbers[0] = 100

# print(list1)
# print(list2)

# print(help(sorted))
# numbers = [1, 2, 3]
# numbers.append([3, 4, 5])

# print(numbers)
# t = numbers.append(5)
# print(t)

# chars = 'ssafy'
# newC = chars.capitalize()
# print(newC)

# T = ''.join(['1', '2'])
# print(T)

numbers = [1, 2, 5, 7, 9]
print(numbers[1:4]) # [2, 5, 7]
print(numbers[1:4:2]) # [2, 7]
print(numbers[1:4:-1]) # []
print(numbers[1:10]) # [2, 5, 7, 9]
print(numbers[4:1:-1]) # [9, 7, 5] 
print(numbers[-1:1:-1]) # [9, 7, 5]
print(numbers[-1:-4:-1]) # [9, 7, 5]
# print(numbers[10])