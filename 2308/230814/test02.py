def check(s):
    pass


def cal(s):
    ST = []
    for c in s:
        if c == ')':
            tmp = 0
            while ST and ST[-1] != '(':
                tmp += int(ST.pop())
            if ST:
                ST.pop()
                ST.append(tmp)
            else:
                return -1

        elif c == '}':
            while ST and ST[-1] != '{':
                tmp *= int(ST.pop())
            if ST:
                ST.pop()
                ST.append(tmp)
            else:
                return -1
        else:
            ST.append(c)
    if len(ST) == 1:
        return ST.pop()
    else:
        return -1
