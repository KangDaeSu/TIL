'''
01D0607 9861D79 F99F
'''

def hextobin(hexS):
    result = ''
    if hexS.isdecimal():
        decV = int(hexS)
    else:
        decV = ord(hexS) - ord('A') + 10

    for i in range(4):
        if decV & (1 << i):
            result = '1' + result
        else:
            result = '0' + result
    return result

# def HexToBin2(HexC):
#     mappintTable = {
#         '0': '0000',
#         '1': '0001',
#         '2': '0010',
#         '3': '0011',
#         '4': '0100',
#         '5': '0101',
#         '6': '0110',
#         '7': '0111',
#         '8': '1000',
#         '9': '1001',
#         'A': '1010',
#         'B': '1011',
#         'C': '1100',
#         'D': '1101',
#         'E': '1110',
#         'F': '1111'
#     }
#     return mappintTable[HexC]

s = '01D06079861D79F99F'
num = ''
for i in s:
    num += hextobin(i)
print(num)
# 순서에 주의할 것
s = s.replace('0', '0000')
s = s.replace('1', '0001')
s = s.replace('2', '0010')
s = s.replace('3', '0011')
s = s.replace('4', '0100')
s = s.replace('5', '0101')
s = s.replace('6', '0110')
s = s.replace('7', '0111')
s = s.replace('8', '1000')
s = s.replace('9', '1001')
s = s.replace('A', '1010')
s = s.replace('B', '1011')
s = s.replace('C', '1100')
s = s.replace('D', '1101')
s = s.replace('E', '1110')
s = s.replace('F', '1111')


def bintodec(binS):
    result = 0
    for c in binS:
        result = result << 1 | int(c)
    return result


result = []
for j in range(0, len(num), 7):
    result.append(bintodec(num[j:j+7]))
print(result)