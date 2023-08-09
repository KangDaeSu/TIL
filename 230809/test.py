# stack : 선형구조
# 후입선출(LIFO) - 마지막에 삽입한 자료를 가장 먼저 꺼냄.
# 스택을 사용하려면 미리 공간을 지정해야 함.


# full이면 True
# 아니면 False
def isFull():
    if top == SIZE - 1:
        return True
    else:
        return False
# 입력이 불가능한 경우 -1을 return
# 입력에 문제가 없는 경우 return top
def push(item):
    global top
    # if isFull():
    if top == SIZE-1:
        print('overflow')
        return -1
    top += 1
    ST[top] = item
    return top

# 스택이 비어 있으면 -1
# 아니면 top 위치에 있는 item을 return
def pop():
    global top # 글로벌 변수 지정 필요
    if top == -1:
    # if isEmpty():
        print('underflow')
        return -1
    result = ST[top]
    top -= 1
    return result # 논리적으로 따지면 이 과정이 맞음.
    # top -= 1
    # return ST[top+1]
def peek(): # 제일 위의 값만 가져오고 싶을 때, isFull로 체크 필수
    return ST[top]
# => print(ST[-1])

SIZE = 10
ST = [-1] * SIZE
top = -1
lst = [4, 5, 6, 10]
# for d in lst:
#     push(d)
# print(ST)
# print(pop(), top)


ST_P = []
for d in lst:
    ST_P.append(d)
if len(ST_P) > 0: # pop전에 길이 체크 필수
    print(ST_P.pop())

#if ST_P: # = len(ST_P) => 리스트에 데이터가 있으면