'''
# 문제 2-2
song = "When you are smiling, the whole world smiles with you"
lst = []

for i in song:
    a = 'a'
    if i == a:
        lst.append(i)
print(len(lst))   

count = 0
for i in song:
    a = 'a'
    if i == a:
        count += 1
print(count)

# 문제 2-3
n = 1
while n < 6:
    print(str(n)*n)
    n += 1


# 문제 2-4
sum1 = 0
sum2 = 0
for i in range(101):
    if i % 3 == 0:
        sum1 += i

    if i % 7 ==0:
        sum2 += i
        
print(f' 0~100의 숫자 중 3의 배수와 7의 배수들의 합은 {sum1+sum2}이다.')


# 문제 2-5
n = int(input())
sum1 = 0
sum2 = 0
for i in range(n+1):
    if i % 7 == 0:
        sum1 += i
    elif str(7) in str(i):
        sum2 += i

print(sum1 + sum2)

# 문제 3-1
while True:
    try:
        a = int(input('정수를 입력하세요. a : '))
        b = int(input('정수를 입력하세요. b : '))
        print(a / b)
        break
    except ValueError:
        print("정수를 입력해야 합니다.")
    except ZeroDivisionError:
        print("b에 0이 아닌 정수를 입력해주세요.")



# 문제 3-2
def BMI(height, weight):
    bmi = weight / (height **2)
    if bmi <= 18.5:
        print("저체중")
    elif 18.5 < bmi <= 23:
        print("정상")
    elif 23 < bmi <= 25:
        print("과체중")  
    elif 25 < bmi <= 30:
        print("비만") 
    elif bmi > 30:
        print("고도비만") 

BMI(1.8,100)


# 문제 3-3
def even_test(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(even_test(5))


# 문제 3-4
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4))


# 문제 3-5
# 1)
# ans = 486
# print("3자리 수를 입력하세요: ")
# numbers = int(input())


# 2)
ans = 486
print("3자리 수를 입력하세요: ")
numbers = int(input())
strike = 0


        
print(strike)



# 3-6
# 1)
def str_n(str, n):
    print(str * n)

str_n('hi', 2)

# 2) 
def str_n(str, n):
    print(str * n)

str_n(str(input()), int(input()))

'''
# 3-7
def digit_sum(n):
    sum = 0
    num = len(str(n))
    for i in range(num):
        s = n % (10 ** i+1)
        

        print(sum)
       
digit_sum(234)


