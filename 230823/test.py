
# 10 => 2진수의 문자열 7 => '111'
def decToBin(decV):
    result = ''
    for shiftBit in range(8):   # 출력하고 싶은 비트 수
        t = decV & (1<<shiftBit)
        if t != 0:
            result = '1' + result
        else:
            result = '0' + result
    return result
print(bin(6))
print(decToBin(6))

# '1101' => 13
def BinToDec(BinS):
    result = 0
    for c in BinS:
        # result = result * 2 + int(c)
        result = result<<1 | int(c)
    return result

print(BinToDec('1101'))

# 16진수 -> 10진수
# '10A' => 266
def HexToDec(HexS):
    result = 0
    for c in HexS:
        if c.isdecimal():
            t = int(c)
        else:
            t = ord(c) - ord('A') + 10
        result = result*16 + t

    return result
print(HexToDec('10A'))

# 16진수 -> 2진수
# 'A' => '1010'
def HexToBin(HexC):
    # 16진수 => 10진수
    result = ''
    if HexC.isdecimal():
        decV = int(HexC)
    else:
        decV = ord(HexC) - ord('A') + 10

    # 10진수 => 2진수
    for shiftBit in range(4):   # 출력하고 싶은 비트 수
        t = decV & (1<<shiftBit)
        if t != 0:
            result = '1' + result
        else:
            result = '0' + result
    return result

print(HexToBin('A'))

def HexToBin2(HexC):
    mappintTable = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    return mappintTable[HexC]

print(HexToBin2('A'))


s ='000000011110000011000000111100110000110000111100111100111111001100111'
for i in range(0, len(s), 7):
    print(BinToDec(s[i:i+7]))